import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6766287844:AAEV-TDgFII0giIZdyDd6VcFWgFPnh1AM3A")
    API_ID = int(os.environ.get("API_ID", 22711559))
    API_HASH = os.environ.get("API_HASH", "07f916d610702eb4b0678bdf32c895c1")
    #Add your channel id. For force Subscribe.
    CHANNEL = os.environ.get("CHANNEL", "-1001967167299")
    #Skip or add your proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = '182.74.243.47:3128'
