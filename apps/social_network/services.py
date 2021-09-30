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
