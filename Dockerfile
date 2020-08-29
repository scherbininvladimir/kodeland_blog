FROM python:3.8.3-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN apk --update add libxml2-dev libxslt-dev libffi-dev libgcc openssl-dev curl
RUN apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev

RUN pip install -r requirements.txt

COPY ./entrypoint.sh /app/entrypoint.sh

COPY ./blog /app/blog
COPY ./kodeland_blog /app/kodeland_blog
COPY ./manage.py /app/manage.py
COPY ./.env /app/.env

ENTRYPOINT ["/app/entrypoint.sh"]