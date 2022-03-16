from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-sr9a8h!8a)cb1-l()xg__y*&^ids@u=5myn%-y+8w^a#(s9g4&'

ALLOWED_HOSTS = ['localhost', '0.0.0.0', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
