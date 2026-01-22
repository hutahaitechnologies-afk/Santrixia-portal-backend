import uuid
from django.db import models


class Country(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    flag = models.CharField(max_length=10)
    image = models.URLField()

    short_description = models.TextField(default="")
    description = models.TextField()
    why = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class VisaType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name="visa_types"
    )
    name = models.CharField(max_length=200)
    description = models.TextField()
    processing_time = models.CharField(max_length=50)
    validity_period = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.country.name} - {self.name}"


class CountryRequirement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name="requirements"
    )
    text = models.TextField()

    def __str__(self):
        return self.text[:40]
