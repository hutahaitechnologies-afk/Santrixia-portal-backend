from django.urls import path
from .views import CountryListAPIView, CountryDetailAPIView

urlpatterns = [
    path("countries/", CountryListAPIView.as_view()),
    path("countries/<slug:slug>/", CountryDetailAPIView.as_view()),
]
