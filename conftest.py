import pytest
import requests
import json
from endpoints.create_meme import CreateMemeNew
from endpoints.change_meme import ChangeMeme
from endpoints.delete_meme import DeleteMeme


@pytest.fixture()
def user_token():
    url = "http://okulik.site:52355/authorize"
    payload = json.dumps({"name": "test_user_1"})
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=payload)
    data = response.json()
    token = data['token']
    return token

@pytest.fixture()
def get_memes_id(user_token):
    url = "http://okulik.site:52355/meme"

    headers = {'Authorization': user_token}
    response = requests.request("GET", url, headers=headers)
    data = response.json()
    return data

@pytest.fixture()
def meme_creator():
    return CreateMemeNew()

@pytest.fixture()
def meme_changer():
    return ChangeMeme()

@pytest.fixture()
def meme_remover():
    return DeleteMeme()