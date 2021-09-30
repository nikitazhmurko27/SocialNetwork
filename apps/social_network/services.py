from django.contrib.auth.models import User

from apps.social_network.models import PostAuthorLike


class PostAuthorLikeModelService:
    def __init__(self, request):
        self.request = request

    def set_like(self, post):
        if post.author != self.request.user:
            try:
                like = PostAuthorLike.objects.get(
                    post=post, author=self.request.user
                )
                like.delete()
            except PostAuthorLike.DoesNotExist:
                PostAuthorLike.objects.create(
                    post=post, author=self.request.user
                )


class UserModelService:
    def __init__(self, validated_data):
        self.validated_data = validated_data

    def create(self):
        user = User(
            email=self.validated_data["email"],
            username=self.validated_data["username"],
        )
        user.set_password(self.validated_data["password"])
        user.save()
        return user
