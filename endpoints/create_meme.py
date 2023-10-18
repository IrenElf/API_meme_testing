import requests
import json


class CreateMemeNew:
    token = None
    text = None
    status = None
    url_meme = None
    info = None
    tags = None

    def create_new_meme(self, url_meme, text, tags, info, user_token):
        url = "http://okulik.site:52355/meme"
        payload = json.dumps({
            "text": text,
            "url": url_meme,
            "tags": tags,
            "info": info
        })
        headers = {'Authorization': user_token, 'Content-Type': 'application/json'}
        response = requests.request("POST", url, headers=headers, data=payload)
        data = response.json()
        self.status = response.status_code
        self.text = data['text']
        self.url_meme = data['url']

        return response

    def check_responce_status_is_ok(self):
        return self.status == 200

    def check_meme_text(self, text):
        return self.text == text

    def check_url_meme_is_ok(self, url_meme):
        return self.url_meme == url_meme

    def check_meme_info(self, info):
        return self.info == info

    def check_meme_tags(self, tags):
        return self.tags == tags
