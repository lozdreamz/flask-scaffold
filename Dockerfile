FROM python:3-alpine

COPY requirements.txt /tmp/requirements.txt

RUN set -ex ; \
    pip install --upgrade pip ; \
    pip install -r /tmp/requirements.txt

ADD . /app

WORKDIR /app

EXPOSE 8000

CMD gunicorn -b 0.0.0.0:8000 "newapp:create_app('prod')"
