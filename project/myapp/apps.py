# myapp/apps.py
from django.apps import AppConfig
from django.contrib.auth.models import User

class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

    def ready(self):
        # Only create superuser if it doesn't exist
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(
                username="kenny",
                email="kennyakanbi@gmail.com",
                password="makmedia"
            )
