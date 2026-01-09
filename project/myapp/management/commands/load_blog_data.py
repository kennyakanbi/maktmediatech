from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.db.utils import IntegrityError

class Command(BaseCommand):
    help = "Load blog fixture safely"

    def handle(self, *args, **kwargs):
        try:
            call_command('loaddata', 'blog_data', verbosity=0)
            self.stdout.write(self.style.SUCCESS('Blog data loaded'))
        except IntegrityError:
            self.stdout.write('Blog data already exists')
        except Exception:
            pass
