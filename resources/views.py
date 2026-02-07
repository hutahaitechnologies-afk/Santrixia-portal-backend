from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .authentication import ApiKeyAuthentication
from .models import Resource
from .serializers import ResourceListSerializer, ResourceDetailSerializer


class ResourceListAPIView(APIView):
    authentication_classes = [ApiKeyAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        resources = Resource.objects.all().order_by("-created_at")
        return Response(
            ResourceListSerializer(resources, many=True).data
        )


class ResourceDetailAPIView(APIView):
    authentication_classes = [ApiKeyAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, resource_id):
        resource = get_object_or_404(
            Resource.objects.prefetch_related("sections", "tips"),
            id=resource_id,
        )
        return Response(
            ResourceDetailSerializer(resource).data
        )
