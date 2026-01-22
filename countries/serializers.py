from rest_framework import serializers
from .models import Country, VisaType


class CountryCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = [
            "id",
            "name",
            "slug",
            "flag",
            "image",
            "short_description",
        ]


class VisaTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisaType
        fields = [
            "id",
            "name",
            "description",
            "processing_time",
            "validity_period",
        ]


class CountryDetailSerializer(serializers.ModelSerializer):
    visaTypes = VisaTypeSerializer(source="visa_types", many=True)
    requirements = serializers.SerializerMethodField()

    class Meta:
        model = Country
        fields = [
            "id",
            "name",
            "full_name",
            "flag",
            "image",
            "description",
            "why",
            "visaTypes",
            "requirements",
        ]

    def get_requirements(self, obj):
        return [r.text for r in obj.requirements.all()]
