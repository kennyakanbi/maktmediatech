from myapp.models import Blog
from django.utils.text import slugify

def seed_blogs():
    if Blog.objects.exists():
        return

    Blog.objects.create(
        title="Welcome to Mak Media Tech Blog",
        description="This is our official blog where we share insights on media, technology, advertising, and digital growth.",
        slug=slugify("Welcome to Mak Media Tech Blog"),
    )
