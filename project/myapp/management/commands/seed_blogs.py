from django.core.management.base import BaseCommand
from django.utils.text import slugify
from myapp.models import Blog  # replace 'myapp' with your app name

class Command(BaseCommand):
    help = "Seed initial blog posts"

    def handle(self, *args, **kwargs):
        if Blog.objects.exists():
            self.stdout.write(self.style.WARNING("Blogs already exist. Nothing to seed."))
            return

        blogs = [
            {
                "title": "Welcome to Mak Media Tech Blog",
                "description": "This is our official blog where we share insights on media, technology, advertising, and digital growth.",
            },
            {
                "title": "Media Advertising Campaigns: Let the World Notice You",
                "description": "Tips and strategies to maximize your brand visibility through media campaigns.",
            },
        ]

        for blog in blogs:
            Blog.objects.create(
                title=blog["title"],
                description=blog["description"],
                slug=slugify(blog["title"]),
            )
            self.stdout.write(self.style.SUCCESS(f'Seeded blog: "{blog["title"]}"'))

        self.stdout.write(self.style.SUCCESS("All blogs have been seeded!"))
