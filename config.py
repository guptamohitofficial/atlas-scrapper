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
LOCAL_MEDIA_FOLDER = get_var('LOCAL_MEDIA_FOLDER', )
