import base64

from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


class AESCipher:
    MAX_KEY_LEN = 32

    def __init__(self, key):
        self.__block_size = AES.block_size
        self.__key = key[:self.MAX_KEY_LEN].encode()

    def encrypt(self, raw: str) -> str:
        raw = pad(raw.encode(), self.__block_size, style='pkcs7')
        iv = Random.new().read(self.__block_size)
        cipher = AES.new(self.__key, AES.MODE_CBC, iv)
        return base64.urlsafe_b64encode(iv + cipher.encrypt(raw)).decode('utf-8')
