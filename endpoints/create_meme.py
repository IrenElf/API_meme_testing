import requests
import json


class CreateMemeNew:

    token = None
    text = None
    status = None
    url_meme = None

    def user_token(self):
        url = "http://okulik.site:52355/authorize"
        payload = json.dumps({"name": "test_user_1"})
        headers = {'Content-Type': 'application/json'}
        response = requests.request("POST", url, headers=headers, data=payload)
        data = response.json()
        self.token = data['token']

    def create_new_meme(self, url_meme, token):
        url = "http://okulik.site:52355/meme"
        payload = json.dumps({
            "text": "Irina's meme",
            "url": "https://i0.wp.com/hyperallergic-newspack.s3.amazonaws.com"
                   "/uploads/2023/04/barbie-lead.jpg?resize=780%2C900&quality=100&ssl=1",
            "tags": [
                "fun",
                "movie",
                "happy"
            ],
            "info": {
                "text1": "Barbie movie",
                "text2": "meme 2023"
            }
        })
        headers = {'Authorization': token, 'Content-Type': 'application/json'}
        response = requests.request("POST", url, headers=headers, data=payload)
        data = response.json()
        self.status = response.status_code
        self.text = data['text']
        self.url_meme = data['url']
        return response

    def check_responce_status_is_ok(self):
        return self.status == 200

    def check_meme_text(self):
        return self.text == "Irina's meme"

    def check_url_meme_is_ok(self):
        return self.url_meme == "https://i0.wp.com/hyperallergic-newspack.s3.amazonaws." \
                                "com/uploads/2023/04/barbie-lead.jpg?resize=780%2C900&quality=100&ssl=1"