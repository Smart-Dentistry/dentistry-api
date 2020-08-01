from django.contrib import admin

from .models import MedicalBackground, Patient

admin.site.register(Patient)
admin.site.register(MedicalBackground)
