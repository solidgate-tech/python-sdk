class FormInitDTO:
    def __init__(self, payment_intent: str, publicKey: str, signature: str):
        self.payment_intent = payment_intent
        self.merchant = publicKey
        self.signature = signature

class FormInitDTO:
    def __init__(self, partial_intent: str, signature: str):
        self.partial_intent = partial_intent
        self.signature = signature