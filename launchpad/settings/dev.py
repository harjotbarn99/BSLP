from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

# secret key
SECRET_KEY = "ks3_w3l#5+5vvy_&bys2q85+q0$0ftw9owuw&6pzk^%k-(_$(h"


INTERNAL_IPS = [
    "127.0.0.1",
]

# database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

