#!/bin/bash
python manage.py migrate
python manage.py createsuperuser --noinput
python manage.py collectstatic --noinput
gunicorn project.wsgi:application
