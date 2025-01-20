import os
import pathlib

import dotenv

from django.core.wsgi import get_wsgi_application

CURREN_DIR = pathlib.Path(__file__).resolve().parent
BASE_DIR = CURRENT_DIR.parent
ENV_FILE_PATH = BASE_DRI / ".env"

dotenv.read_dotenv(str(ENV_FILE_PATH))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_k8s.settings')

application = get_wsgi_application()