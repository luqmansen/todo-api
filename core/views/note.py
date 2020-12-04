from datetime import timedelta

from django.utils.datetime_safe import datetime
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

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

    def get_note_by_category(self, request, *args, **kwargs):
        queryset = self.queryset.filter(
            user=request.user,
            category=kwargs['cat']
        )
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
