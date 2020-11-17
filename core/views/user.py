from django.contrib.auth.models import User
from rest_framework import viewsets

from core.permissions import IsPostOrIsAuthenticated
from core.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsPostOrIsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
