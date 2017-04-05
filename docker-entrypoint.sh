#!/bin/bash
set -ev

python manage.py makemigrations
python manage.py migrate
