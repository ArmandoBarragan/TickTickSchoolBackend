import os
from config.settings.base import *

SECRET_KEY = os.getenv('SECRET_KEY')


ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS')
WHITELIST = os.getenv('WHITELIST')


DATABASES = {
    'default': {
        'ENGINE': "django.db.backends.postgresql",
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('PORT'),
        'PORT': os.getenv('DB_PORT'),
    }
}

LANGUAGE_CODE = 'es'
TIME_ZONE = os.getenv('TIMEZONE')
USE_I18N = os.getenv('USE_I18N')
USE_L10N = os.getenv('USE_L10N')
USE_TZ = os.getenv('USE_TZ')

DEBUG = True
