from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model

User = get_user_model()
PASSWORD = 'pi3.1415'
DEVS = [
    {'username': 'm', 'password': PASSWORD, 'email': 'm@mathsistor.com'},
    {'username': 'sika', 'password': PASSWORD, 'email': 'sikabarca@gmail.com'}
]


class Command(BaseCommand):
    help = 'Seeds database'

    def handle(self, *args, **options):
        for dev in DEVS:
            try:
                User.objects.create_superuser(**dev)
            except Exception:
                raise CommandError('Database was not seed.')

        self.stdout.write(self.style.SUCCESS('Database was seed successfully!'))
