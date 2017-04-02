FROM python:2-onbuild
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

RUN python manage.py runserver 0.0.0.0:9999

EXPOSE 9999
