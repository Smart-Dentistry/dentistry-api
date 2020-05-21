from django.db import models
from django.contrib.postgres.fields import JSONField
from django_extensions.db.models import TimeStampedModel

from phonenumber_field.modelfields import PhoneNumberField


class Patient(TimeStampedModel):
    profile_picture_url = models.URLField(blank=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    second_last_name = models.CharField(max_length=50, blank=True)
    id_document_number = models.CharField(max_length=25)

    class Sex(models.TextChoices):
        MALE = "M", "Male"
        FEMALE = "F", "Female"

    sex = models.CharField(max_length=1, choices=Sex.choices)
    job_title = models.CharField(max_length=100, blank=True)

    class MaritalStatus(models.TextChoices):
        MARRIED = "MA", "Married"
        SINGLE = "SI", "Single"
        DIVORCED = "DI", "Divorced"
        WIDOWED = "WI", "Widowed"
        DOMESTIC_PARTNERSHIP = "DP", "Domestic partnership"
        NOT_SPECIFIED = "NS", "Not specified"

    marital_status = models.CharField(
        max_length=2, choices=MaritalStatus.choices, default=MaritalStatus.NOT_SPECIFIED
    )
    birthdate = models.DateField()

    class CountryOfResidence(models.TextChoices):
        ECUADOR = "E", "Ecuador"
        ABROAD = "A", "Abroad"

    country_of_residence = models.CharField(
        max_length=1,
        choices=CountryOfResidence.choices,
        default=CountryOfResidence.ECUADOR,
    )
    address = JSONField(blank=True, null=True)
    phone = PhoneNumberField()
    whatsapp = models.BooleanField(default=False)
    health_insurance_company = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    receive_promos = models.BooleanField(default=True)

    class ReferralSourceChoices(models.TextChoices):
        PERSONAL_REFERENCE = "P", "Personal reference"
        SOCIAL_MEDIA = "S", "Social media"
        OTHER = "O", "Other"

    referral_source = models.CharField(
        max_length=1, choices=ReferralSourceChoices.choices
    )
    emergency_contact = JSONField(blank=True, null=True)
    representative = JSONField(blank=True, null=True)
    family_history = JSONField(blank=True, null=True)
    personal_history = JSONField(blank=True, null=True)
    general_practitioners = JSONField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
