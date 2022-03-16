import os

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