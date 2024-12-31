from ninja.security import HttpBearer
from decouple import config


class GlobalAuth(HttpBearer):
    def authenticate(self, request, token):
        api_key = config("API_KEY", default=None)
        if token == api_key:
            return token
