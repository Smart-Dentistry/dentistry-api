from django.contrib import admin

from .models import MedicalBackground, Patient, PeriodontalExam

admin.site.register(Patient)
admin.site.register(MedicalBackground)
admin.site.register(PeriodontalExam)
