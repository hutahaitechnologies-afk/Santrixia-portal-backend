from django.contrib import admin
from .models import ApiKey, Resource, ResourceSection, ResourceTip


@admin.register(ApiKey)
class ApiKeyAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "key", "is_active", "created_at")
    readonly_fields = ("key",)


class ResourceSectionInline(admin.TabularInline):
    model = ResourceSection
    extra = 1


class ResourceTipInline(admin.TabularInline):
    model = ResourceTip
    extra = 1


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "published_date", "read_time_minutes", "created_at")
    list_filter = ("category", "published_date", "created_at")
    search_fields = ("title", "category", "excerpt")
    ordering = ("-created_at",)
    inlines = [ResourceSectionInline, ResourceTipInline]


# @admin.register(ResourceSection)
# class ResourceSectionAdmin(admin.ModelAdmin):
#     list_display = ("resource", "heading", "order")
#     list_filter = ("resource",)
#     search_fields = ("heading", "content")
#     ordering = ("resource", "order", "id")


# @admin.register(ResourceTip)
# class ResourceTipAdmin(admin.ModelAdmin):
#     list_display = ("resource", "text", "order")
#     list_filter = ("resource",)
#     search_fields = ("text",)
#     ordering = ("resource", "order", "id")
