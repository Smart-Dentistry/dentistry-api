import string

from django.contrib.auth import get_user_model

import factory
from factory.fuzzy import FuzzyText, FuzzyChoice

from medical_records.models import Patient

User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    password = factory.PostGenerationMethodCall("set_password", "pi3.1415")


class PatientFactory(factory.django.DjangoModelFactory):
    last_name = factory.Faker("last_name")
    id_document_number = FuzzyText(length=10, chars=string.digits)
    job_title = factory.Faker("job")
    birthdate = factory.Faker("date")
    phone = FuzzyChoice(
        [
            "+593983761752",
            "+13053991321",
            "+593987309076",
            "+16262005695",
            "+918668999704",
        ]
    )
    whatsapp = FuzzyChoice([True, False, True, True])
    health_insurance_company = FuzzyChoice(
        ["Health Inc", "Moderna", "BMI", "Google Health", "Apple Health"]
    )
    email = factory.Faker("free_email")
    referral_source = FuzzyChoice(Patient.ReferralSourceChoices.values)

    class Meta:
        abstract = True
        model = Patient


class MalePatientFactory(PatientFactory):
    first_name = factory.Faker("first_name_male")
    sex = "M"


class FemalePatientFactory(PatientFactory):
    first_name = factory.Faker("first_name_female")
    sex = "F"
