from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from resources.authentication import ApiKeyAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Country
from .serializers import (
    CountryCardSerializer,
    CountryDetailSerializer,
)


class CountryListAPIView(APIView):
    authentication_classes = [ApiKeyAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        countries = Country.objects.all().order_by("name")
        return Response(
            CountryCardSerializer(countries, many=True).data
        )


class CountryDetailAPIView(APIView):
    authentication_classes = [ApiKeyAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, slug):
        try:
            country = Country.objects.get(slug=slug)
        except Country.DoesNotExist:
            raise NotFound("Country not found")

        return Response(
            CountryDetailSerializer(country).data
        )
