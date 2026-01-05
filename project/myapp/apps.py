from django.apps import AppConfig


class MyappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "myapp"

    def ready(self):
        from django.contrib.auth import get_user_model
        from django.utils.text import slugify
        from myapp.models import Blog

        User = get_user_model()

        # Get any existing user (admin)
        author = User.objects.first()
        if not author:
            return  # safety guard

        Blog.objects.get_or_create(
            slug="welcome-to-mak-media-tech-blog",
            defaults={
                "author_name": author,
                "title": "Welcome to Mak Media Tech Blog",
                "description": (
                    "This is our official blog where we share insights on "
                    "media, technology, digital marketing, and brand growth."
                ),
            },
        )
