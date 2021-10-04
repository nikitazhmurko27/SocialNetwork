from django.contrib.auth.models import User
from rest_framework import serializers

from apps.social_network.models import Post
from apps.social_network.services import PostModelService


class PostAuthorSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source="username")
    author = serializers.CharField(source="id")

    class Meta:
        model = User
        fields = ["author", "author_name"]
        read_only_fields = ["author", "author_name"]


class PostSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="iso-8601", read_only=True)

    likes = PostAuthorSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ["id", "title", "content", "author", "likes", "created_at"]
        read_only_fields = ["author"]

    def create(self, validated_data):
        user = self.context["request"].user
        service = PostModelService(validated_data)
        post = service.create(user)
        return post
