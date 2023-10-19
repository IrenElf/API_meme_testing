import requests
import json


class DeleteMeme:
    token = None
    text = None
    status = None
    url_meme = None
    info = None
    tags = None
    mem_id = None
    response = None

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

    def delete_meme(self, mem_id, user_token):
        url = "http://okulik.site:52355/meme/" + mem_id

        payload = {}
        headers = {'Authorization': user_token}
        self.response = requests.request("DELETE", url, headers=headers, data=payload)

    def check_delete_meme_is_ok(self):
        return self.response == f'Meme with id{self.mem_id}successfully deleted'
