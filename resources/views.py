from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .authentication import ApiKeyAuthentication
from .models import Resource
from .serializers import ResourceSerializer


class ResourceListAPIView(APIView):
    authentication_classes = [ApiKeyAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        resources = Resource.objects.all().order_by("-created_at")
        return Response(
            ResourceSerializer(resources, many=True).data
        )
