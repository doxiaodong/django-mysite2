FROM python:2-onbuild
WORKDIR /usr/src/app
COPY . .

EXPOSE 9999

CMD ["python", "manage.py", "makemigrations"]
CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:9999"]
