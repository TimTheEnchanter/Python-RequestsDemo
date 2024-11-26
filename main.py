import requests
from requests.exceptions import HTTPError

try:
    response = requests.get("https://api.github.com")
    response.raise_for_status()
except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
except Exception as err:
        print(f"Other error occurred: {err}")
else:
        print("Success!")
