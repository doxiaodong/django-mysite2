FROM python:3.7
WORKDIR /usr/src/app
VOLUME /usr/src/app/config
COPY . /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 9999
CMD ["./start.sh"]
