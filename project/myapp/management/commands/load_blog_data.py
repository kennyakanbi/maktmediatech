# myapp/management/commands/load_blog_data.py
from django.core.management.base import BaseCommand
from django.core.management import call_command
from myapp.models import Blog

class Command(BaseCommand):
    help = "Load blog fixture if no blogs exist"

    def handle(self, *args, **kwargs):
        if Blog.objects.exists():
            self.stdout.write(self.style.SUCCESS("Blogs already loaded, skipping"))
        else:
            call_command('loaddata', 'myapp/fixtures/blog_data.json')
            self.stdout.write(self.style.SUCCESS("Blog fixture loaded successfully"))
