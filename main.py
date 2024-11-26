import requests
from requests.exceptions import HTTPError

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
print(response3.json())