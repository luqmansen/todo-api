from django.contrib.auth.models import User
from rest_framework import serializers

from core.models import Notes, Category


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']


class NotesSerializer(serializers.ModelSerializer):
    is_complete = serializers.BooleanField(required=False)

    class Meta:
        model = Notes
        exclude = ['user']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ['user']


