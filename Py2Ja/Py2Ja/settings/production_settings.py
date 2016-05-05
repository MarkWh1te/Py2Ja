# -*- coding: utf-8 -*-

from base_settings import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['.beinghacker.xyz', ]

ADMINS = [
    ('Summy', 'summychou@gmail.com'),
]


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'databases/pro_db.sqlite3'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}


# Production Mode
STATIC_ROOT = os.path.join(BASE_DIR, 'static').replace('\\', '/')
