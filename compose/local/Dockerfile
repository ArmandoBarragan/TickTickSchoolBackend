FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

WORKDIR /code

COPY requirements/local.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY . /code