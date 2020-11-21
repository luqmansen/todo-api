from django.conf.urls import url
from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

from core.api_schema import core_api_schema

urlpatterns = [
    path('', lambda req: TemplateResponse(req, 'index.html', {})),
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
]

# auth
urlpatterns += [
    path('api/auth/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

# docs
urlpatterns += [
   url(r'^swagger(?P<format>\.json|\.yaml)$', core_api_schema.without_ui(cache_timeout=0), name='schema-json'),
   url(r'^swagger/$', core_api_schema.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   url(r'^redoc/$', core_api_schema.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]