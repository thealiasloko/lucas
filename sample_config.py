import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5060402747:AAFS3p644EL-OeugK6yC55omqr-XW7caXLU")

    APP_ID = int(os.environ.get("APP_ID", "9454157"))

    API_HASH = os.environ.get("API_HASH", "f9a0e6045b7cb8f7dab987d0c2cbb4a3")
