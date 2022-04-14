import os

from config.settings.base import *


SECRET_KEY = '-m%z0q$46ii!)3ms7pzb59*kh=6$co7wsq^h%93r%qpnd&+^-w'

CONTAINER_ENVIRON = os.getenv('CONTAINER_ENVIRON')

POSTGRES_DATABASE = {

    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'tts_db',

        'USER': 'postgres',

        'PASSWORD': 'postgres',

        'HOST': 'db',

        'PORT': 5432,

    }

}

SQLITE_DATABASE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DATABASES = POSTGRES_DATABASE if CONTAINER_ENVIRON else SQLITE_DATABASE

LANGUAGE_CODE = 'es'
TIME_ZONE = 'America/Chihuahua'
USE_I18N = True
USE_L10N = True
USE_TZ = True

DEBUG = True
ALLOWED_HOSTS = ["*"]
