# myapp/apps.py
from django.apps import AppConfig
from django.conf import settings

class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

    def ready(self):
        # Only try this in production to avoid creating on every run
        import django
        from django.contrib.auth import get_user_model
        from django.db.utils import OperationalError, ProgrammingError

        User = get_user_model()
        try:
            if not User.objects.filter(username="admin").exists():
                User.objects.create_superuser(
                    username="admin",
                    email="admin@example.com",
                    password="Admin123!"
                )
        except (OperationalError, ProgrammingError):
            # DB not ready yet (migrations not applied) — ignore
            pass
