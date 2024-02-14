#!/bin/bash
APP_PORT=${PORT:-8000}
cd /code
python3 manage.py migrate --no-input
python3 manage.py collectstatic --no-input
gunicorn --worker-tmp-dir /dev/shm config.wsgi:application --bind "${HOST}:${APP_PORT}"