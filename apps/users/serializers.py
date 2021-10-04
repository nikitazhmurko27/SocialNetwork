from django.contrib.auth.models import User
from rest_framework import serializers

from apps.users.services import UserModelService


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        service = UserModelService(validated_data)
        user = service.create()
        return user
