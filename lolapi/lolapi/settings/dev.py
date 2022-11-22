import os
from ._base import *

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lolapi.settings.dev')

DEBUG = True
SECRET_KEY = 'django-insecure-h!gy%^*f8(yqr!+=c*x(5(le8&*!iuz_e1e(p%ets+7u9cb@cw'