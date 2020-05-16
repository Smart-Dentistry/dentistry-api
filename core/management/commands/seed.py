from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = 'Seeds database'

    def handle(self, *args, **options):
        try:
            User.objects.create_superuser(
                username='m',
                password='pi3.1415'
            )
        except Exception:
            raise CommandError('Database was not seed.')

        self.stdout.write(self.style.SUCCESS('Database was seed successfully!'))
