import requests


endpoint = "http://127.0.0.1:8000/api/"
response= requests.get(endpoint, params={'name':'ming'}, json={'query':'hi therer'})

print(response.json())