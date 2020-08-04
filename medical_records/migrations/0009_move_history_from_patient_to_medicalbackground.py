from django.db import migrations


def forwards_func(apps, schema_editor):
    Patient = apps.get_model("medical_records", "Patient")
    MedicalBackground = apps.get_model("medical_records", "MedicalBackground")
    for patient in Patient.objects.all():
        try:
            medical_background = patient.medical_background
        except MedicalBackground.DoesNotExist:
            medical_background = MedicalBackground()
        
        medical_background.patient = patient
        medical_background.family_history = patient.family_history
        medical_background.personal_history = patient.personal_history
        medical_background.general_practitioners = patient.general_practitioners
        medical_background.save()


def reverse_func(apps, schema_editor):
    Patient = apps.get_model("medical_records", "Patient")
    MedicalBackground = apps.get_model("medical_records", "MedicalBackground")

    for patient in Patient.objects.all():
        try:
            medical_background = patient.medical_background
        except MedicalBackground.DoesNotExist:
            continue
        else:
            patient.family_history = medical_background.family_history
            patient.personal_history = medical_background.personal_history
            patient.general_practitioners = medical_background.general_practitioners
            medical_background.delete()
            patient.save()

class Migration(migrations.Migration):

    dependencies = [("medical_records", "0008_rename_medicalbackground_to_medical_background")]

    operations = [migrations.RunPython(forwards_func, reverse_func)]
