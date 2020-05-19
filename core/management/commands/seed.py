from django.core.management.base import BaseCommand, CommandError
from core.factories import UserFactory, MalePatientFactory, FemalePatientFactory

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

        for _ in range(10):
            MalePatientFactory()
            FemalePatientFactory()

        self.stdout.write(self.style.SUCCESS('Database was seed successfully!'))
