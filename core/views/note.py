from datetime import timedelta

from django.utils.datetime_safe import datetime
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from core.models import Notes
from core.serializers import NotesSerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
    permission_classes = (IsAuthenticated,)

    def filter_queryset(self, queryset):
        return queryset.filter(
            user=self.request.user,
        ).order_by('created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
