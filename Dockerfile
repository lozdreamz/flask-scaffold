FROM python:3-alpine

ENV FLASK_APP=autoapp.py
ENV DAPP_SECRET=somesecretbytes
ENV FLASK_DEBUG=1
# ENV PYTHONWARNINGS=ignore::DeprecationWarning

COPY requirements.txt /tmp/requirements.txt

RUN set -ex ; \
    pip install --upgrade pip ; \
    pip install -r /tmp/requirements.txt

ADD . /app

WORKDIR /app

EXPOSE 8000

CMD gunicorn -b 0.0.0.0:8000 "newapp:create_app('prod')"
