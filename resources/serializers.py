from rest_framework import serializers
from .models import Resource, ResourceSection


class ResourceListSerializer(serializers.ModelSerializer):
    date = serializers.CharField(source="published_date_display", read_only=True)
    readTime = serializers.CharField(source="read_time_display", read_only=True)
    image = serializers.CharField(source="image_url")

    class Meta:
        model = Resource
        fields = [
            "id",
            "title",
            "category",
            "date",
            "readTime",
            "excerpt",
            "image",
        ]


class ResourceSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceSection
        fields = ["heading", "content"]


class ResourceDetailSerializer(serializers.ModelSerializer):
    image = serializers.CharField(source="detail_image_url")
    sections = ResourceSectionSerializer(many=True, read_only=True)
    tips = serializers.ListField(
        child=serializers.CharField(),
        source="tips_text_list",
        read_only=True
    )

    class Meta:
        model = Resource
        fields = ["title", "image", "description", "sections", "tips"]
