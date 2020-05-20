from rest_framework import serializers

from medical_records.models import Patient


class PatientSerializer(serializers.ModelSerializer):
    key = serializers.IntegerField(source="id", read_only=True)

    class Meta:
        model = Patient
        fields = [
            "key",
            "photo",
            "first_name",
            "middle_name",
            "last_name",
            "second_last_name",
            "id_document_number",
            "sex",
            "job_title",
            "marital_status",
            "birthdate",
            "country_of_residence",
            "address",
            "phone",
            "whatsapp",
            "health_insurance_company",
            "email",
            "receive_promos",
            "referral_source",
            "emergency_contact",
            "representative",
            "family_history",
            "personal_history",
            "general_practitioners",
        ]


class PatientTableSerializer(serializers.ModelSerializer):
    key = serializers.IntegerField(source="id", read_only=True)

    class Meta:
        model = Patient
        fields = [
            "key",
            "photo",
            "first_name",
            "last_name",
            "id_document_number",
            "email",
            "phone",
            "birthdate",
            "whatsapp",
        ]
