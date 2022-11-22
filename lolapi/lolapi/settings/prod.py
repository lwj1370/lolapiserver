import os
from ._base import *

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lolapi.settings.prod')

DEBUG = False
SECRET_KEY = 'django-secure-production-encrypt-code'