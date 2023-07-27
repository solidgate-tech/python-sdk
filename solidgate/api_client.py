import base64
import hashlib
import hmac
import json
from datetime import datetime
from typing import Generator

import requests

from solidgate.encryption import AESCipher
from solidgate.model import MerchantData


class ApiClient:
    BASE_SOLID_GATE_API_URI = 'https://pay.solidgate.com/api/v1/'
    BASE_RECONCILIATION_API_URI = 'https://reports.solidgate.com/'

    RECONCILIATION_ORDERS_PATH = 'api/v2/reconciliation/orders'
    RECONCILIATION_CHARGEBACKS_PATH = 'api/v2/reconciliation/chargebacks'

    RECONCILIATION_DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'

    def __init__(self, merchant_id: str,
                 private_key: str,
                 base_solid_gate_api_uri: str = BASE_SOLID_GATE_API_URI,
                 base_reconciliations_api_uri: str = BASE_RECONCILIATION_API_URI):
        self.__merchant_id = merchant_id
        self.__private_key = private_key
        self.__base_solid_gate_api_uri = base_solid_gate_api_uri
        self.__base_reconciliations_api_uri = base_reconciliations_api_uri

    def charge(self, attributes: dict) -> requests.models.Response:
        return self.__send_solidgate_request('charge', attributes)

    def recurring(self, attributes: dict) -> requests.models.Response:
        return self.__send_solidgate_request('recurring', attributes)

    def resign(self, attributes: dict) -> requests.models.Response:
        return self.__send_solidgate_request('resign', attributes)

    def status(self, attributes: dict) -> requests.models.Response:
        return self.__send_solidgate_request('status', attributes)

    def refund(self, attributes: dict) -> requests.models.Response:
        return self.__send_solidgate_request('refund', attributes)

    def auth(self, attributes: dict) -> requests.models.Response:
        return self.__send_solidgate_request('auth', attributes)

    def void(self, attributes: dict) -> requests.models.Response:
        return self.__send_solidgate_request('void', attributes)

    def settle(self, attributes: dict) -> requests.models.Response:
        return self.__send_solidgate_request('settle', attributes)

    def arn_code(self, attributes: dict) -> requests.models.Response:
        return self.__send_solidgate_request('arn-code', attributes)

    def apple_pay(self, attributes: dict) -> requests.models.Response:
        return self.__send_solidgate_request('apple-pay', attributes)

    def google_pay(self, attributes: dict) -> requests.models.Response:
        return self.__send_solidgate_request('google-pay', attributes)

    def form_merchant_data(self, attributes: dict) -> FormInitDTO:
        payment_intent = AESCipher(self.__private_key).encrypt(self.__convert_request_attributes_to_str(attributes))
        signature = self.__generate_signature(payment_intent)
        form_init_dto = FormInitDTO(payment_intent=payment_intent, publicKey=self.__merchant_id, signature=signature)
        return form_init_dto

    def form_update(self, attributes: dict) -> FormUpdateDTO:
        partial_intent = AESCipher(self.__private_key).encrypt(self.__convert_request_attributes_to_str(attributes))
        signature = self.__generate_signature(partial_intent)
        form_update_dto = FormUpdateDTO(partial_intent=partial_intent, signature=signature)
        return form_update_dto

    def order_reconciliation(self, date_from: datetime, date_to: datetime) -> Generator:
        return self.__send_reconciliation_request(self.RECONCILIATION_ORDERS_PATH, date_from, date_to)

    def chargeback_reconciliation(self, date_from: datetime, date_to: datetime) -> Generator:
        return self.__send_reconciliation_request(self.RECONCILIATION_CHARGEBACKS_PATH, date_from, date_to)

    def __generate_signature(self, data: str) -> str:
        encrypto_data = (self.__merchant_id + data + self.__merchant_id).encode('utf-8')
        sign = hmac.new(self.__private_key.encode('utf-8'), encrypto_data, hashlib.sha512).hexdigest()
        return base64.b64encode(sign.encode('utf-8')).decode('utf-8')

    def __send_solidgate_request(self, method: str, attributes: dict) -> requests.models.Response:
        full_url = self.__base_solid_gate_api_uri + method
        return self.__send_request(full_url, attributes)

    def __send_reconciliation_request(self, path: str, date_from: datetime, date_to: datetime) -> Generator:
        full_url = self.__base_reconciliations_api_uri + path
        attributes = {'date_from': date_from.strftime(self.RECONCILIATION_DATETIME_FORMAT),
                      'date_to': date_to.strftime(self.RECONCILIATION_DATETIME_FORMAT)}
        while True:
            try:
                response = self.__send_request(full_url, attributes)
            except requests.exceptions.RequestException as err:
                raise Exception("Exception during request:", err)

            if 200 <= response.status_code < 300:
                response_content = json.loads(response.content)
                for order in response_content['orders']:
                    yield order

                attributes['next_page_iterator'] = response_content['metadata']['next_page_iterator']
                if not attributes['next_page_iterator']:
                    break
            else:
                raise Exception('Request is not successful!')

    def __send_request(self, path: str, attributes: dict) -> requests.models.Response:
        body = self.__convert_request_attributes_to_str(attributes)
        headers = {'Content-Type': 'application/json',
                   'Accept': 'application/json',
                   'Merchant': self.__merchant_id,
                   'Signature': self.__generate_signature(body)}
        return requests.post(path, headers=headers, json=attributes)

    @staticmethod
    def __convert_request_attributes_to_str(attributes: dict) -> str:
        return json.dumps(attributes)
