FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

WORKDIR /code
COPY requirements/production.txt ./requirements.txt
RUN pip install -r requirements.txt