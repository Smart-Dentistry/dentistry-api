import datetime
import string

from django.contrib.auth import get_user_model
from django.conf import settings

import factory
from factory.fuzzy import FuzzyText, FuzzyChoice, FuzzyDate

from medical_records.models import Patient

User = get_user_model()
S3_BASE_URL = f"https://{settings.AWS_S3_CUSTOM_DOMAIN}"
FEMALE_PHOTOS = [f"{S3_BASE_URL}/photo_0.png", f"{S3_BASE_URL}/photo_1.png"]
MALE_PHOTOS = [f"{S3_BASE_URL}/photo_2.png", f"{S3_BASE_URL}/photo_3.png"]


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    password = factory.PostGenerationMethodCall("set_password", "pi3.1415")


class PatientFactory(factory.django.DjangoModelFactory):
    last_name = factory.Faker("last_name")
    id_document_number = FuzzyText(length=10, chars=string.digits)
    job_title = factory.Faker("job")
    birthdate = FuzzyDate(datetime.date(1920, 1, 1))
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
    profile_picture_url = FuzzyChoice(MALE_PHOTOS)
    first_name = factory.Faker("first_name_male")
    sex = "M"


class FemalePatientFactory(PatientFactory):
    profile_picture_url = FuzzyChoice(FEMALE_PHOTOS)
    first_name = factory.Faker("first_name_female")
    sex = "F"
