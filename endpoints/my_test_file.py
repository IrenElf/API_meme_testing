import requests
import json


def get_token():
    url = "http://okulik.site:52355/authorize"
    payload = json.dumps({
        "name": "test_user_1"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    data = response.json()
    token = data['token']
    print(token)


print(get_token())

