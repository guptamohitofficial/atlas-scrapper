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

LOGGER_LEVEL = get_var('LOGGER_LEVEL', "debug")

DB_TYPE = get_var('DB_TYPE', "sqlite")
DB_NAME = get_var('DB_NAME')
DB_USER = get_var('DB_USER')
DB_PASSWORD = get_var('DB_PASSWORD')
DB_HOST = get_var('DB_HOST')

SMTP_SERVER = get_var("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = get_var("SMTP_PORT", 587)
SMTP_USERNAME = get_var("SMTP_USERNAME", "mohithelpservices@gmail.com")
SMTP_PASSWORD = get_var("SMTP_PASSWORD", "rtawhyrcthmpfnbu")

# I have used GupShup whatsapp integration,
# I can share credentials personally if not available,
# Please reachout personally, not confortable adding into github
WHATSAPP_API_BASE_ENDPOINT = get_var("WHATSAPP_API_BASE_ENDPOINT", "https://api.gupshup.io/sm/api/v1")
WHATSAPP_API_SOURCE_PHONE = get_var("WHATSAPP_API_SOURCE_PHONE") # please let me know
WHATSAPP_API_APP_NAME = get_var("WHATSAPP_API_APP_NAME") # please let me know
WHATSAPP_API_KEY = get_var("WHATSAPP_API_KEY") # please let me know
WHATSAPP_API_TEMPLATE_ID_Atlys_SCRAPPER_NOTIFICATION = get_var("WHATSAPP_API_TEMPLATE_ID_Atlys_SCRAPPER_NOTIFICATION", "07804f10-a269-49df-a759-1ce9c6b78a91")


NOTIFICATION_USERS = [
    {
        "name": "Mohit", # first name
        "whatsapp": "8357051635", # only 10 digits
        "email": "moohitgupta1@gmail.com",
        "is_active": True
    },
    {
        "name": "Udbhav", # first name
        "whatsapp": "", # only 10 digits
        "email": "udbhav@atlys.com",
        "is_active": False # make it true when you wants to use it
    },
]
