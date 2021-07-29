class MerchantData:
    def __init__(self, payment_intent: str, merchant: str, signature: str):
        self.payment_intent = payment_intent
        self.merchant = merchant
        self.signature = signature
