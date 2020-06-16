from django.utils.timezone import now
from rest_framework import serializers
from drf_yasg.utils import swagger_serializer_method

from medical_records.models import Patient


class PatientSerializer(serializers.ModelSerializer):
    key = serializers.IntegerField(source="id", read_only=True)
    age = serializers.SerializerMethodField()
    whatsapp_link = serializers.SerializerMethodField()

    @swagger_serializer_method(serializer_or_field=serializers.IntegerField)
    def get_age(self, obj):
        today = now().date()
        return (
            today.year
            - obj.birthdate.year
            - ((today.month, today.day) < (obj.birthdate.month, obj.birthdate.day))
        )

    def get_whatsapp_link(self, obj):
        if obj.whatsapp:
            return f"https://wa.me/{obj.phone.raw_input[1:]}"

    class Meta:
        model = Patient
        fields = [
            "key",
            "profile_picture_url",
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
            "whatsapp_link",
            "health_insurance_company",
            "email",
            "receive_promos",
            "referral_source",
            "emergency_contact",
            "representative",
            "family_history",
            "personal_history",
            "general_practitioners",
            "age",
        ]


class ValueLabelSerializer(serializers.Serializer):
    value = serializers.IntegerField()
    label = serializers.CharField()
