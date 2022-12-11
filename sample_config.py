import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5967174827:AAHpXZNA6E0sp8agatm_Z_R3jSuNnUGhtS4")

    APP_ID = int(os.environ.get("APP_ID", "11849455"))

    API_HASH = os.environ.get("API_HASH", "0956032efc5694f60156fe65f9c19764")
