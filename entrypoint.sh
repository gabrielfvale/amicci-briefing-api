#!/bin/bash

python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "Creating superuser"
source ./.env
python manage.py createsuperuser \
    --noinput \
    --username $DJANGO_SUPERUSER_USERNAME \
    --email $DJANGO_SUPERUSER_EMAIL

exec "$@"
