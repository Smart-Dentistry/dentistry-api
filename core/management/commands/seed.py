from django.core.management.base import BaseCommand, CommandError
from core.factories import UserFactory

DEVS = [
    {'username': 'm', 'email': 'm@mathsistor.com'},
    {'username': 'sika', 'email': 'sikabarca@gmail.com'}
]


class Command(BaseCommand):
    help = 'Seeds database'

    def handle(self, *args, **options):
        for dev in DEVS:
            try:
                UserFactory(**dev, is_superuser=True, is_staff=True)
            except Exception:
                raise CommandError('Database was not seed.')

        self.stdout.write(self.style.SUCCESS('Database was seed successfully!'))
