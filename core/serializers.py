from django.contrib.auth import get_user_model
from rest_framework import serializers

from core.models import Notes, Category

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        return user

    class Meta:
        model = UserModel
        fields = ('password', 'username', 'first_name', 'last_name',)


class NotesSerializer(serializers.ModelSerializer):
    is_complete = serializers.BooleanField(required=False)

    class Meta:
        model = Notes
        exclude = ['user']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ['user']
