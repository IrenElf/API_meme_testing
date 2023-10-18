import requests
from endpoints.create_meme import CreateMemeNew


def test_create_new_meme():
    endpoint = CreateMemeNew()
    endpoint.check_responce_status_is_ok()
    endpoint.check_meme_text()
    endpoint.check_url_meme_is_ok()
