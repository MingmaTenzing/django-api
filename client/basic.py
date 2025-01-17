import requests
import json

endpoint = "http://127.0.0.1:8000/api/get-token/"
response= requests.post(endpoint, json={
    'username': "user",
    'password': "password689++"
})

token = response.json()['token']
print(token)


if token: 
    requestList = requests.get("http://127.0.0.1:8000/api/product/list", headers={
        'Authorization': f"Bearer {token}"
    })
    print(requestList.json())