
from config.settings.base import *


SECRET_KEY = '-m%z0q$46ii!)3ms7pzb59*kh=6$co7wsq^h%93r%qpnd&+^-w'
TEST_RUNNER = "django.test.runner.DiscoverRunner"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

LANGUAGE_CODE = 'es'
TIME_ZONE = 'America/Chihuahua'
USE_I18N = True
USE_L10N = True
USE_TZ = True

DEBUG = True
ALLOWED_HOSTS = ["*"]
