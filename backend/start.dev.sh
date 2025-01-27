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
python manage.py loaddata material/fixtures/store
python manage.py loaddata material/fixtures/wood_species
python manage.py loaddata material/fixtures/material_status

python manage.py runserver 0.0.0.0:8001
