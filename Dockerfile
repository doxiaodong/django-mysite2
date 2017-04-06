FROM python:2-onbuild
WORKDIR /usr/src/app
COPY . .

RUN ls

# RUN apt-get update && apt-get install -y \
# 		gcc \
#		gettext \
#		mysql-client libmysqlclient-dev \
#		libpq-dev \
#		sqlite3 \
#	--no-install-recommends && rm -rf /var/lib/apt/lists/*

COPY docker-entrypoint.sh /usr/local/bin/
RUN ln -s usr/local/bin/docker-entrypoint.sh /entrypoint.sh # backwards compat

ENTRYPOINT ["docker-entrypoint.sh"]

EXPOSE 9999
CMD ["python", "manage.py", "runserver", "0.0.0.0:9999"]
