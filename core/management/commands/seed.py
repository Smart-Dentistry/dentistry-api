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
            "province": "Azuay",
            "city": "Cuenca",
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
        male.family_history = {
            "diseases": [
                {"id": 1, "relatives": [1, 2, 3]},
                {"id": 2, "relatives": [4, 6]},
            ],
            "observations": "This is a great patient.",
        }
        male.personal_history = {
            "diseases": [3, 4],
            "observations": "No acute diseases.",
        }
        male.general_practitioners = [
            {"disease": "Lupus", "name": "Greg House", "phone": "+5932456756"},
            {"disease": "COVID-19", "name": "Jim Morrison", "phone": "+59333333"},
        ]
        male.save()

    def handle(self, *args, **options):
        self._create_devs()
        self._create_patients()

        self.stdout.write(self.style.SUCCESS("Database was seed successfully!"))
