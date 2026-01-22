from rest_framework import serializers
from .models import Resource


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = [
            "id",
            "title",
            "description",
            "read_time_minutes",
            "created_at",
        ]
