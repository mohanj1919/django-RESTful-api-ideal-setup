FROM python:3.5
ENV PYTHONUNBUFFERED 1
ARG build_env

RUN mkdir /app

ADD requirements/ /app/requirements/
WORKDIR /app/requirements/
RUN pip install -Ur ./$build_env.txt

ADD . /app/
WORKDIR /app/
