from ninja.security import HttpBearer
from decouple import config


class GlobalAuth(HttpBearer):
    """
    Class to authenticate access to API

    Args:
        HttpBearer ():
    """

    def authenticate(self, request, token):
        """
        Method to authenticate to api based on token provided

        Args:
            request (request): the request object
            token (token): the API token to authenticate

        Returns:
            token (api_key): the api key
        """
        api_key = config("VITE_API_KEY", default=None)
        if token == api_key:
            return token
