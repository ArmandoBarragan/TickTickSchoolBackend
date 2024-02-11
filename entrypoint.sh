#!/bin/bash
APP_PORT=${PORT:-8000}
cd /code
gunicorn --worker-tmp-dir /dev/shm config.wsgi:application --bind "${HOST}:${PORT}"