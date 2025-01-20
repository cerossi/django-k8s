import os

DB_DATABASE = os.environ.get("POSTGRES_DB")
DB_USER = os.environ.get("POSTGRES_USER")
DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
DB_HOST = os.environ.get("POSTGRES_HOST")
DB_PORT = os.environ.get("POSTGRES_PORT")
DB_IS_AVAIL = all([DB_DATABASE, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT])

POSTGRES_READY = str(os.environ.get("POSTGRES_READY")) == "1"

if POSTGRES_READY and DB_IS_AVAIL:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": DB_DATABASE,
            "USER": DB_USER,
            "PASSWORD": DB_PASSWORD,
            "HOST": DB_HOST,
            "PORT": DB_PORT,
        }
    }
