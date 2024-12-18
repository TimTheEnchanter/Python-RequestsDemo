import requests
from requests.exceptions import HTTPError
from requests.auth import HTTPBasicAuth
from custom_token_auth import TokenAuth
from requests.exceptions import Timeout

response = requests.get(
    "https://api.github.com/search/repositories",
    params={"q": "language:python", "sort": "stars", "order": "desc"},
)

response2 = requests.get(
    "https://api.github.com/search/repositories",
    params={"q": '"real python"'},
    headers={"Accept": "application/vnd.github.text-match+json"},
)

json_response = response.json()
popular_repositories = json_response["items"]
for repo in popular_repositories[:5]:
    print(f"Name: {repo['name']}")
    print(f"Description: {repo['description']}")
    print(f"Stars: {repo['stargazers_count']}")
    print()
    
json_response2 = response2.json()
first_repository = json_response2["items"][0]
print(first_repository["text_matches"][0]["matches"])

response3 = requests.post("https://httpbin.org/post", data=[("key", "value")])
print(response3.request.url)
print(response3.request.body)

response4 = requests.get(
     "https://httpbin.org/basic-auth/user/passwd",
     auth=HTTPBasicAuth("user", "passwd")
)

print(response4.status_code)
print(response4.request.headers["Authorization"])


token = "<PA ACCESS TOKEN GOES HERE>"
response5 = requests.get(
     "https://api.github.com/user",
     auth=("", token)
)

print(response5.status_code)
print(response5.request.headers["Authorization"])

response6 = requests.get(
     "https://api.github.com/user",
     auth=TokenAuth(token)
)

print(response6.request.headers["Authorization"])

response7 = requests.get("https://api.github.com", verify=False)

print(response7)

try:
    response8 = requests.get("https://api.github.com", timeout=(3.05, 5))
    print(response8)
except Timeout:
    print("The request timed out")
else:
    print("The request did not time out")

