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

    # Related models are used for visa details (see below)

    def __str__(self):
        return f"{self.country.name} - {self.name}"


# Program Overview
class VisaProgramOverview(models.Model):
    visa_type = models.OneToOneField(VisaType, on_delete=models.CASCADE, related_name="program_overview")
    first_heading = models.CharField(max_length=200)
    last_paragraph = models.TextField()

# Program Overview Points
class VisaProgramOverviewPoint(models.Model):
    program_overview = models.ForeignKey(VisaProgramOverview, on_delete=models.CASCADE, related_name="points")
    icon = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField()

# Benefits
class VisaBenefit(models.Model):
    visa_type = models.ForeignKey(VisaType, on_delete=models.CASCADE, related_name="benefits")
    icon = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()

# Eligibility Requirements
class VisaEligibilityRequirement(models.Model):
    visa_type = models.ForeignKey(VisaType, on_delete=models.CASCADE, related_name="eligibility_requirements")
    title = models.CharField(max_length=100)
    description = models.TextField()
    detail = models.TextField(blank=True)

# CRS Factors
class VisaCRSFactor(models.Model):
    visa_type = models.ForeignKey(VisaType, on_delete=models.CASCADE, related_name="crs_factors")
    category = models.CharField(max_length=100)
    points = models.CharField(max_length=50)
    factors = models.TextField(help_text="Comma-separated list of factors")

# Process Steps
class VisaProcessStep(models.Model):
    visa_type = models.ForeignKey(VisaType, on_delete=models.CASCADE, related_name="process_steps")
    step = models.PositiveIntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.CharField(max_length=50, blank=True)

# Fees
class VisaFee(models.Model):
    visa_type = models.ForeignKey(VisaType, on_delete=models.CASCADE, related_name="fees")
    item = models.CharField(max_length=100)
    cost = models.CharField(max_length=50)
    note = models.TextField(blank=True)

# Processing Time & Fees
class VisaProcessingTimeAndFee(models.Model):
    visa_type = models.ForeignKey(VisaType, on_delete=models.CASCADE, related_name="processing_time_and_fees")
    icon = models.CharField(max_length=100)
    header = models.CharField(max_length=100)
    time = models.CharField(max_length=50)
    short_description = models.TextField()
    note = models.TextField(blank=True)


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
