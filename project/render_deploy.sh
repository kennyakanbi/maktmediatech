#!/bin/bash
# Activate virtual environment
source .venv/bin/activate

# Run migrations
python manage.py migrate

# Load fixture safely
# This avoids duplicate slug errors by ignoring already-loaded entries
python manage.py loaddata myapp/fixtures/blog_data.json || echo "Some fixtures may already exist, skipping duplicates."

# Collect static files
python manage.py collectstatic --noinput
