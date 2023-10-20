
def test_delete_meme(meme_remover, user_token):
    url_meme = "https://i0.wp.com/hyperallergic-newspack.s3.amazonaws.com"\
          "/uploads/2023/04/barbie-lead.jpg?resize=780%2C900&quality=100&ssl=1"
    text = "Irina's meme"
    tags = ["fun", "movie", "happy"]
    info = {"text1": "Barbie movie", "text2": "meme 2023"}
    user_token = user_token
    meme_remover.create_new_meme(url_meme, text, tags, info, user_token)
    meme_remover.check_delete_meme_is_ok()
