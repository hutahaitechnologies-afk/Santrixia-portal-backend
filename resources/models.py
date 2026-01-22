import uuid
from django.db import models
import uuid
from django.conf import settings
from django.db import models


class Resource(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    read_time_minutes = models.PositiveIntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title





class ApiKey(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="api_keys"
    )
    name = models.CharField(max_length=100)
    key = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.name}"
