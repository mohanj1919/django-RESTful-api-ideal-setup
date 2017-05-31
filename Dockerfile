FROM python:3.5
ARG build_env

RUN mkdir /app

WORKDIR /app/

ADD requirements/ /app/requirements/
WORKDIR /app/requirements/
RUN pip install -Ur ./$build_env.txt

ADD . /app/
WORKDIR /app/

EXPOSE 8000

#CMD python manage.py runserver --settings=config.settings.$build_env
