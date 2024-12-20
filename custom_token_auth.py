from requests.auth import AuthBase

class TokenAuth(AuthBase):

    def __init__(self, token):
        self.token = token

    def __call__(self, request):
        request.headers["Authorization"] = f"Bearer {self.token}"
        return request