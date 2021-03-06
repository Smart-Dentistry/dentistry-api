from django.contrib import admin

from .models import (ClinicalExam,
                     MedicalBackground,
                     NonPathologicalBackground,
                     Patient,
                     PeriodontalExam)

admin.site.register(Patient)
admin.site.register(MedicalBackground)
admin.site.register(PeriodontalExam)
admin.site.register(NonPathologicalBackground)
admin.site.register(ClinicalExam)
