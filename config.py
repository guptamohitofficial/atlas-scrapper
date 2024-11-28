import os
from dotenv import load_dotenv
load_dotenv()

def get_var(val, default=None):
    try:
        val = os.getenv(val)
        if val: return val
    except: pass
    return default

DEBUG = get_var('DEBUG', "false") == "true"

LOCAL_MEDIA_FOLDER = get_var('LOCAL_MEDIA_FOLDER', 'saved_media')

LOGGER_LEVEL = os.getenv('LOGGER_LEVEL', "debug")

DB_TYPE = os.getenv('DB_TYPE', "sqlite")
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')

NOTIFICATION_USERS = [
    {
        "name": "Mohit Gupta", # full name
        "whatsapp": "8357051635", # only 10 digits
        "email": "moohitgupta1@gmail.com",
        "is_active": True
    },
    {
        "name": "Udbhav Rai", # full name
        "whatsapp": "", # only 10 digits
        "email": "udbhav@atlys.com",
        "is_active": False # make it true when you wants to use it
    },
]
