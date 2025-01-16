import requests
import json

endpoint = "http://127.0.0.1:8000/api/get-token/"
response= requests.post(endpoint, json={
    'username': "ming",
    'password': "password689++"
})

token = response.json()['token']


if token: 
    requestList = requests.get("http://127.0.0.1:8000/api/product/list", headers={
        'Authorization': f"Token {token}"
    })
    print(requestList.json())