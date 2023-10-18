
def test_change_meme(meme_changer, user_token):
    url_meme = "https://i0.wp.com/hyperallergic-newspack.s3.amazonaws.com"\
          "/uploads/2023/04/barbie-lead.jpg?resize=780%2C900&quality=100&ssl=1"
    text = "Irina's meme"
    tags = ["fun", "movie", "happy"]
    info = {"text1": "Barbie movie", "text2": "meme 2023"}
    text_new = "New movie meme"
    info_new = {"text1": "Barbie movie_new", "text2": "meme 2023_new"}
    meme_changer.check_change_meme_info(info_new)
    meme_changer.check_change_meme_text(text_new)