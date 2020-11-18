from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('', lambda req: TemplateResponse(req, 'index.html', {})),
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
    path('auth/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
