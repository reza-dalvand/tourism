from django.test import Client


class TestSetup:
    def setup_method(self):
        self.client = Client()
        self.prefix_url = "http://localhost:8000/api/v1"
        self.auth_url = f"{self.prefix_url}/users/auth/"
        self.verify_auth_url = f"{self.prefix_url}/users/auth/verify/"
