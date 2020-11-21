from django.conf.urls import url
from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt import views as jwt_views

auth_urlpatterns = [
    path('api/auth/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns = [
    path('', lambda req: TemplateResponse(req, 'index.html', {})),
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
] + auth_urlpatterns

#  DRF YASG Stuff
schema_view = get_schema_view(
   openapi.Info(
      title="Chems Todo API",
      default_version='v1',
      description="API description here",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="MIT License"),
   ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns += [
   url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
