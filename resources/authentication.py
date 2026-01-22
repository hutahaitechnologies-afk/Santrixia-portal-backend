from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import ApiKey


class ApiKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        api_key = request.headers.get("X-API-KEY")

        if not api_key:
            return None

        try:
            api_key_obj = ApiKey.objects.select_related("user").get(
                key=api_key,
                is_active=True
            )
        except ApiKey.DoesNotExist:
            raise AuthenticationFailed("Invalid API Key")

        # ✅ Return real Django user
        request.api_key = api_key_obj
        return (api_key_obj.user, None)
