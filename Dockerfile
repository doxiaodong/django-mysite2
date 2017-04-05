FROM python:2.7

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ONBUILD COPY requirements.txt /usr/src/app/
ONBUILD RUN pip install --no-cache-dir -r requirements.txt

ONBUILD COPY . /usr/src/app

RUN apt-get update && apt-get install -y \
		gcc \
		gettext \
		mysql-client libmysqlclient-dev \
		libpq-dev \
		sqlite3 \
	--no-install-recommends && rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["docker-entrypoint.sh"]

EXPOSE 9999
CMD ["python", "manage.py", "runserver", "0.0.0.0:9999"]
