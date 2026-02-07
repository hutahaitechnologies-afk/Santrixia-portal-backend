import uuid
from django.conf import settings
from django.db import models


class Resource(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    published_date = models.DateField()
    read_time_minutes = models.PositiveIntegerField(default=5)
    excerpt = models.TextField()
    image_url = models.URLField()
    detail_image_url = models.URLField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def read_time_display(self):
        return f"{self.read_time_minutes} min read"

    @property
    def published_date_display(self):
        return self.published_date.strftime("%B %d, %Y").replace(" 0", " ")

    @property
    def tips_text_list(self):
        return [tip.text for tip in self.tips.all()]


class ResourceSection(models.Model):
    resource = models.ForeignKey(
        Resource,
        on_delete=models.CASCADE,
        related_name="sections"
    )
    heading = models.CharField(max_length=255)
    content = models.TextField()
    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.resource.title} - {self.heading}"


class ResourceTip(models.Model):
    resource = models.ForeignKey(
        Resource,
        on_delete=models.CASCADE,
        related_name="tips"
    )
    text = models.TextField()
    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.resource.title} - {self.text[:40]}"




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
