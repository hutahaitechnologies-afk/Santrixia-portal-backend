from django.contrib import admin
from .models import ApiKey, Resource


@admin.register(ApiKey)
class ApiKeyAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "key", "is_active", "created_at")
    readonly_fields = ("key",)


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ("title", "read_time_minutes", "created_at")
