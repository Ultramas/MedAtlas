import os
from paypalcheckoutsdk.core import PayPalHttpClient, LiveEnvironment, SandboxEnvironment

class PayPalClient:
    def __init__(self):
        client_id     = os.getenv("PAYPAL_CLIENT_ID")
        client_secret = os.getenv("PAYPAL_SECRET")
        if os.getenv("PAYPAL_ENV") == "live":
            env = LiveEnvironment(client_id, client_secret)
        else:
            env = SandboxEnvironment(client_id, client_secret)
        self.client = PayPalHttpClient(env)
