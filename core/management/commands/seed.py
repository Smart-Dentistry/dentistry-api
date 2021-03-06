from django.core.management.base import BaseCommand, CommandError
from core.factories import UserFactory, MalePatientFactory, FemalePatientFactory

DEVS = [
    {"username": "m", "email": "m@mathsistor.com"},
    {"username": "sika", "email": "sikabarca@gmail.com"},
]


class Command(BaseCommand):
    help = "Seeds database"

    def _create_devs(self):
        for dev in DEVS:
            try:
                UserFactory(**dev, is_superuser=True, is_staff=True)
            except Exception:
                raise CommandError("Database was not seed.")

    def _create_patients(self):
        for _ in range(10):
            male = MalePatientFactory()
            FemalePatientFactory()
        male.address = {
            "province": "1",
            "canton": "3",
            "address_line": "Gringolandia",
        }
        male.emergency_contact = {
            "full_name": "John McDonalds",
            "phone": "+593954342534",
        }
        male.representative = {
            "full_name": "Elvis Williams",
            "phone": "+593900000534",
            "relationship": "Father",
        }
        male.save()

    def handle(self, *args, **options):
        self._create_devs()
        self._create_patients()

        self.stdout.write(self.style.SUCCESS("Database was seed successfully!"))
