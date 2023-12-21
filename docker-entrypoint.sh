#!/bin/sh
echo 'Run makemigrations'
python manage.py makemigrations
echo 'Run migrate'
python manage.py migrate
echo 'Collect Static'
python manage.py collectstatic --noinput
exec "$@"