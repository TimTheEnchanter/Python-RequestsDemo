import requests
from custom_token_auth import TokenAuth

TOKEN = "<PA ACCESS TOKEN GOES HERE>"

with requests.Session() as session:
    session.auth = TokenAuth(TOKEN)

    first_response = session.get("https://api.github.com/user")
    second_response = session.get("https://api.github.com/user")

print(first_response.headers)
print(second_response.json())