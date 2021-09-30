from django.contrib.auth.models import User
from rest_framework import serializers

from apps.social_network.models import Post, PostAuthorLike
from apps.social_network.services import UserModelService


class PostAuthorSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source="author.username")
    author = serializers.ReadOnlyField(source="author.id")

    class Meta:
        model = PostAuthorLike
        fields = ["author", "author_name"]


class PostSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="iso-8601", read_only=True)

    likes = PostAuthorSerializer(
        many=True, source="post_authors_likes", read_only=True
    )

    class Meta:
        model = Post
        fields = ["id", "title", "content", "author", "likes", "created_at"]
        read_only_fields = ["author"]

    def create(self, validated_data):
        user = self.context["request"].user
        post = Post.objects.create(author=user, **validated_data)
        return post


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        service = UserModelService(validated_data)
        user = service.create()
        return user
