FROM python:3.6-onbuild
WORKDIR /usr/src/app
VOLUME /usr/src/app/config
COPY . /usr/src/app

EXPOSE 9999
CMD ["./start.sh"]
