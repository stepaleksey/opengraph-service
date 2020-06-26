FROM python:3.7.7-alpine3.10
LABEL maintainer="Aleksey Stepanov;"
ENV PYTHONPATH /usr/local/lib/python3.7/site-packages
RUN apk add --update --no-cache --virtual .build-deps \
        g++ \
        libxml2 py3-gunicorn \
        libxml2-dev && \
    apk add libxslt-dev


EXPOSE 5000

RUN pip3 install libxml2-python3 flask requests pytest

WORKDIR /app/
COPY src /app/

