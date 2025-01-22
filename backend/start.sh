#!/bin/bash

python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py collectstatic --no-input
#python manage.py createcachetable

if [ "$DJANGO_SUPERUSER_USERNAME" ]; then
    (python manage.py createsuperuser \
        --noinput \
        --username $DJANGO_SUPERUSER_USERNAME \
        --email $DJANGO_SUPERUSER_EMAIL) ||
        true
fi

python manage.py loaddata administration/fixtures/version
python manage.py loaddata project/fixtures/project_status
python manage.py loaddata task/fixtures/task_status
python manage.py loaddata project/fixtures/project_phase
python manage.py loaddata part/fixtures/part_status

gunicorn backend.wsgi:application --bind 0.0.0.0:8000
