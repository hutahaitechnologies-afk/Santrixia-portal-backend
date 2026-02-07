from django.contrib import admin
from .models import (
    Country, VisaProgramOverviewPoint, VisaType, CountryRequirement,
    VisaProgramOverview, VisaBenefit, VisaEligibilityRequirement, VisaCRSFactor,
    VisaProcessStep, VisaFee, VisaProcessingTimeAndFee
)
class VisaProgramOverviewPointInline(admin.TabularInline):
    model = VisaProgramOverviewPoint
    extra = 1
    fields = ("icon", "title", "description")

class VisaProgramOverviewInline(admin.StackedInline):
    model = VisaProgramOverview
    extra = 0
    max_num = 1
    inlines = [VisaProgramOverviewPointInline]

class VisaBenefitInline(admin.TabularInline):
    model = VisaBenefit
    extra = 1

class VisaEligibilityRequirementInline(admin.TabularInline):
    model = VisaEligibilityRequirement
    extra = 1

class VisaCRSFactorInline(admin.TabularInline):
    model = VisaCRSFactor
    extra = 1

class VisaProcessStepInline(admin.TabularInline):
    model = VisaProcessStep
    extra = 1

class VisaFeeInline(admin.TabularInline):
    model = VisaFee
    extra = 1

class VisaProcessingTimeAndFeeInline(admin.TabularInline):
    model = VisaProcessingTimeAndFee
    extra = 1
@admin.register(VisaType)
class VisaTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "country", "processing_time", "validity_period")
    search_fields = ("name",)
    inlines = [
        VisaProgramOverviewInline,
        VisaBenefitInline,
        VisaEligibilityRequirementInline,
        VisaCRSFactorInline,
        VisaProcessStepInline,
        VisaFeeInline,
        VisaProcessingTimeAndFeeInline,
    ]
@admin.register(VisaProgramOverview)
class VisaProgramOverviewAdmin(admin.ModelAdmin):
    list_display = ("visa_type", "first_heading")
    inlines = [VisaProgramOverviewPointInline]



class VisaTypeInline(admin.TabularInline):
    model = VisaType
    extra = 1
    fields = (
        "name",
        "description",
        "processing_time",
        "validity_period",
    )


class CountryRequirementInline(admin.TabularInline):
    model = CountryRequirement
    extra = 1
    fields = ("text",)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "full_name",
        "slug",
        "created_at",
    )
    search_fields = ("name", "full_name")
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ("id", "created_at")

    fieldsets = (
        ("Basic Info", {
            "fields": (
                "id",
                "name",
                "full_name",
                "slug",
                "flag",
                "image",
            )
        }),
        ("Descriptions", {
            "fields": (
                "short_description",
                "description",
                "why",
            )
        }),
        ("Meta", {
            "fields": ("created_at",)
        }),
    )

    inlines = [
        VisaTypeInline,
        CountryRequirementInline,
    ]
