from django.urls import path
from .views import ResourceListAPIView, ResourceDetailAPIView

urlpatterns = [
    path("resources/", ResourceListAPIView.as_view(), name="resource-list"),
    path("resources/<int:resource_id>/", ResourceDetailAPIView.as_view(), name="resource-detail"),
]
