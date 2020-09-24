FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir /webapps

ENV BUILD_PACKAGES linux-headers curl curl-dev tzdata \
    ca-certificates gcc postgresql-dev build-base bash postgresql-client

RUN apk add --update --no-cache $BUILD_PACKAGES

ENV TZ America/Sao_Paulo

RUN cp /usr/share/zoneinfo/$TZ /etc/localtime

# RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN pip install -U pip setuptools

COPY requirements.txt /webapps/

RUN pip install -r /webapps/requirements.txt

ADD . /webapps
WORKDIR /webapps

EXPOSE 5000
