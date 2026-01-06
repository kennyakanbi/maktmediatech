# myapp/apps.py
from django.apps import AppConfig
from django.contrib.auth import get_user_model
import logging

logger = logging.getLogger(__name__)

class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

    def ready(self):
        User = get_user_model()
        try:
            if not User.objects.filter(username="kenny").exists():
                User.objects.create_superuser(
                    username="kenny",
                    email="kennyakanbi@gmail.com",
                    password="makmedia"
                )
                logger.info("Superuser 'kenny' created successfully.")
        except Exception as e:
            logger.warning(f"Could not create superuser: {e}")
