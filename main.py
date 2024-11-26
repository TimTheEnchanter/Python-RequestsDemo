import requests

response = requests.get("https://api.github.com")

if response.status_code == 200:
    print("Success!")
elif response.status_code == 404:
    raise Exception(f"Request Failed - status code: {response.status_code}")