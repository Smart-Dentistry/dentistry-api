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
    first_appointment_reason = models.TextField(default="", blank=True)

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

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class MedicalBackground(TimeStampedModel):
    patient = models.OneToOneField(
        Patient,
        on_delete=models.CASCADE,
        related_name="medical_background",
        related_query_name="medical_background",
    )
    family_history = JSONField(blank=True, null=True)
    personal_history = JSONField(blank=True, null=True)
    general_practitioners = JSONField(blank=True, null=True)
    drinker = models.BooleanField(default=False)
    smoker = models.BooleanField(default=False)

    def __str__(self):
        return str(self.patient)


class PeriodontalExam(TimeStampedModel):
    patient = models.OneToOneField(
        Patient,
        on_delete=models.CASCADE,
    )
    dental_plaque = models.BooleanField(default=False)
    calculus = models.BooleanField(default=False)
    bleeding = models.BooleanField(default=False)
    tooth_mobility = models.BooleanField(default=False)

    def __str__(self):
        return str(self.patient)


class NonPathologicalBackground(TimeStampedModel):
    patient = models.OneToOneField(
        Patient,
        on_delete=models.CASCADE,
    )

    class BrushingFrequencyChoices(models.IntegerChoices):
        ZERO = 0
        ONE = 1
        TWO = 2
        THREE = 3
        MORE = 4

    brushing_frequency = models.IntegerField(
        choices=BrushingFrequencyChoices.choices, blank=True, null=True
    )
    mouthwash = models.BooleanField(default=False)
    floss = models.BooleanField(default=False)

    def __str__(self):
        return str(self.patient)


class ClinicalExam(TimeStampedModel):
    patient = models.OneToOneField(
        Patient,
        on_delete=models.CASCADE,
    )
    intraoral_exam = models.TextField(blank=True)
    extraoral_exam = models.TextField(blank=True)

    def __str__(self):
        return str(self.patient)
