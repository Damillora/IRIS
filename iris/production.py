from iris.settings import *
import os

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('IRIS_DB_NAME'),
        'USER': os.getenv('IRIS_DB_USER'),
        'PASSWORD': os.getenv('IRIS_DB_PASS'),
        'HOST': os.getenv('IRIS_DB_HOST'),
    }
}

ALLOWED_HOSTS = [ os.getenv('IRIS_HOST') ]

CSRF_TRUSTED_ORIGINS = [ os.getenv('IRIS_WEB_URL') ]