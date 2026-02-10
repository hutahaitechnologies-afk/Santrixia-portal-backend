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
            "full_name",
            "short_description",
        ]


from .visa_program_overview_point_serializer import VisaProgramOverviewPointSerializer

class VisaProgramOverviewSerializer(serializers.ModelSerializer):
    points = VisaProgramOverviewPointSerializer(many=True, read_only=True)
    class Meta:
        model = __import__('countries.models').models.VisaProgramOverview
        fields = ["first_heading", "points", "last_paragraph"]

class VisaBenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = __import__('countries.models').models.VisaBenefit
        fields = ["icon", "title", "description"]

class VisaEligibilityRequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = __import__('countries.models').models.VisaEligibilityRequirement
        fields = ["title", "description", "detail"]

class VisaCRSFactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = __import__('countries.models').models.VisaCRSFactor
        fields = ["category", "points", "factors"]

class VisaProcessStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = __import__('countries.models').models.VisaProcessStep
        fields = ["step", "title", "description", "duration"]

class VisaFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = __import__('countries.models').models.VisaFee
        fields = ["item", "cost", "note"]

class VisaProcessingTimeAndFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = __import__('countries.models').models.VisaProcessingTimeAndFee
        fields = ["icon", "header", "time", "short_description", "note"]

class VisaTypeSerializer(serializers.ModelSerializer):
    program_overview = VisaProgramOverviewSerializer(read_only=True)
    benefits = VisaBenefitSerializer(many=True, read_only=True)
    eligibility_requirements = VisaEligibilityRequirementSerializer(many=True, read_only=True)
    crs_factors = VisaCRSFactorSerializer(many=True, read_only=True)
    process_steps = VisaProcessStepSerializer(many=True, read_only=True)
    fees = VisaFeeSerializer(many=True, read_only=True)
    processing_time_and_fees = VisaProcessingTimeAndFeeSerializer(many=True, read_only=True)

    class Meta:
        model = VisaType
        fields = [
            "id",
            "name",
            "description",
            "processing_time",
            "validity_period",
            "program_overview",
            "benefits",
            "eligibility_requirements",
            "crs_factors",
            "process_steps",
            "fees",
            "processing_time_and_fees",
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
