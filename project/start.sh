#!/bin/bash
python manage.py migrate
python manage.py createsuperuser --noinput
gunicorn project.wsgi:application
