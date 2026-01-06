from django.apps import AppConfig

class MyappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "myapp"

    def ready(self):
        import os
        if os.environ.get("RENDER"):
            try:
                from django.core.management import call_command
                call_command("create_default_superuser")
            except Exception:
                pass
