#!/bin/bash

# Exit on error
set -e

echo "Starting deployment script..."

# 1️⃣ Apply migrations
echo "Applying migrations..."
python manage.py migrate --noinput

# 2️⃣ Create superuser if not exists
echo "Checking for superuser..."
DJANGO_SUPERUSER_USERNAME=${DJANGO_SUPERUSER_USERNAME}
DJANGO_SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL}
DJANGO_SUPERUSER_PASSWORD=${DJANGO_SUPERUSER_PASSWORD}

python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); \
if not User.objects.filter(username='$DJANGO_SUPERUSER_USERNAME').exists(): \
    User.objects.create_superuser('$DJANGO_SUPERUSER_USERNAME', '$DJANGO_SUPERUSER_EMAIL', '$DJANGO_SUPERUSER_PASSWORD')"

# 3️⃣ Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# 4️⃣ Start Gunicorn
echo "Starting Gunicorn..."
gunicorn project.wsgi:application --bind 0.0.0.0:\$PORT
