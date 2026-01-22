from django.contrib import admin
from .models import Country, VisaType, CountryRequirement


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
