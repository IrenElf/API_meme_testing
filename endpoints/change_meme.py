import requests
import json


class ChangeMeme:
    token = None
    text = None
    status = None
    url_meme = None
    info = None
    tags = None
    mem_id = None

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
        self.mem_id = data['id']

        return response

    def change_meme(self, mem_id, url_meme, text_new, tags, info_new, user_token):
        url = "http://okulik.site:52355/meme/" + mem_id

        payload = json.dumps({
            "id": mem_id,
            "text": text_new,
            "url": url_meme,
            "tags": tags,
            "info": info_new
        })
        headers = {'Authorization': user_token, 'Content-Type': 'application/json'}
        response = requests.request("PUT", url, headers=headers, data=payload)
        data = response.json()
        self.text = data['text']
        self.info = data['info']

    def check_change_meme_text(self, text_new):
        return self.text == text_new

    def check_change_meme_info(self, info_new):
        return self.info == info_new
