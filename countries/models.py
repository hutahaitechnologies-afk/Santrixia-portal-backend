import uuid
from django.db import models


class Country(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField()
    full_name = models.CharField()
    slug = models.SlugField(unique=True)
    flag = models.CharField()
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
    name = models.CharField()
    description = models.TextField()
    processing_time = models.CharField()
    validity_period = models.CharField()

    # Related models are used for visa details (see below)

    def __str__(self):
        return f"{self.country.name} - {self.name}"


# Program Overview
class VisaProgramOverview(models.Model):
    visa_type = models.OneToOneField(VisaType, on_delete=models.CASCADE, related_name="program_overview")
    first_heading = models.CharField()
    last_paragraph = models.TextField()

# Program Overview Points
class VisaProgramOverviewPoint(models.Model):
    program_overview = models.ForeignKey(VisaProgramOverview, on_delete=models.CASCADE, related_name="points")
    icon = models.CharField()
    title = models.CharField()
    description = models.TextField()

# Benefits
class VisaBenefit(models.Model):
    visa_type = models.ForeignKey(VisaType, on_delete=models.CASCADE, related_name="benefits")
    icon = models.CharField()
    title = models.CharField()
    description = models.TextField()

# Eligibility Requirements
class VisaEligibilityRequirement(models.Model):
    visa_type = models.ForeignKey(VisaType, on_delete=models.CASCADE, related_name="eligibility_requirements")
    title = models.CharField()
    description = models.TextField()
    detail = models.TextField(blank=True)

# CRS Factors
class VisaCRSFactor(models.Model):
    visa_type = models.ForeignKey(VisaType, on_delete=models.CASCADE, related_name="crs_factors")
    category = models.CharField()
    points = models.CharField()
    factors = models.TextField(help_text="Comma-separated list of factors")

# Process Steps
class VisaProcessStep(models.Model):
    visa_type = models.ForeignKey(VisaType, on_delete=models.CASCADE, related_name="process_steps")
    step = models.PositiveIntegerField()
    title = models.CharField()
    description = models.TextField()
    duration = models.CharField( blank=True)

# Fees
class VisaFee(models.Model):
    visa_type = models.ForeignKey(VisaType, on_delete=models.CASCADE, related_name="fees")
    item = models.CharField()
    cost = models.CharField()
    note = models.TextField(blank=True)

# Processing Time & Fees
class VisaProcessingTimeAndFee(models.Model):
    visa_type = models.ForeignKey(VisaType, on_delete=models.CASCADE, related_name="processing_time_and_fees")
    icon = models.CharField()
    header = models.CharField()
    time = models.CharField()
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
