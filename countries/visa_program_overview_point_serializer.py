from rest_framework import serializers
from .models import VisaProgramOverviewPoint

class VisaProgramOverviewPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisaProgramOverviewPoint
        fields = ["id", "icon", "title", "description"]
