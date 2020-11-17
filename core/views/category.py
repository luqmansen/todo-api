from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from core.models import Category
from core.serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)

    def filter_queryset(self, queryset):
        return queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
