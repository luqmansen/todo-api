from django.urls import path

from core.views.user import UserViewSet

user_list = UserViewSet.as_view({'get': 'retrieve'})

urlpatterns = [
    path('user/me/', user_list),
]