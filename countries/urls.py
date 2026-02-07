from django.urls import path
from .views import CountryListAPIView, CountryDetailAPIView, VisaTypeDetailAPIView

urlpatterns = [
    path("countries/", CountryListAPIView.as_view()),
    path("countries/<slug:slug>/", CountryDetailAPIView.as_view()),
    path("visa/<uuid:visa_id>/", VisaTypeDetailAPIView.as_view()),
]
