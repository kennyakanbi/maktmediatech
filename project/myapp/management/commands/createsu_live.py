from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

User = get_user_model()

class Command(BaseCommand):
    help = "Create superuser on Render if not exists"

    def handle(self, *args, **options):
        # Only run on Render
        if not os.environ.get("DATABASE_URL"):
            self.stdout.write("DATABASE_URL not set. Skipping superuser creation.")
            return

        username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
        email = os.environ.get("DJANGO_SUPERUSER_EMAIL")
        password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

        if not username or not password:
            self.stdout.write("Superuser env vars not set. Skipping.")
            return

        if User.objects.filter(username=username).exists():
            self.stdout.write("Superuser already exists.")
            return

        User.objects.create_superuser(
            username=username,
            email=email,
            password=password,
        )

        self.stdout.write("Superuser created successfully.")
