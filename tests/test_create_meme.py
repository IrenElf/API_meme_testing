
def test_create_new_meme(meme_creator, user_token):
    url_meme = "https://i0.wp.com/hyperallergic-newspack.s3.amazonaws.com"\
          "/uploads/2023/04/barbie-lead.jpg?resize=780%2C900&quality=100&ssl=1"
    text = "Irina's meme"
    tags = ["fun", "movie", "happy"]
    info = {"text1": "Barbie movie", "text2": "meme 2023"}
    user_token = user_token
    meme_creator.create_new_meme(url_meme, text, tags, info, user_token)
    meme_creator.check_responce_status_is_ok()
    meme_creator.check_meme_text(text)
    meme_creator.check_url_meme_is_ok(url_meme)
    meme_creator.check_meme_info(info)
    meme_creator.check_meme_tags(tags)
