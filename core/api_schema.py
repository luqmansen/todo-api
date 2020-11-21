from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

core_api_schema = get_schema_view(
   openapi.Info(
      title="Chems Todo API",
      default_version='v1',
      description="Just to do list API",
      contact=openapi.Contact(email="luqmansen@gmail.com"),
      license=openapi.License(name="MIT License"),
   ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
