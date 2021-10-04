from apps.social_network.models import Post


class PostModelService:
    def __init__(self, data):
        self.data = data

    def create(self, author):
        post = Post.objects.create(author=author, **self.data)
        return post


class PostAuthorLikeModelService:
    def __init__(self, request):
        self.request = request

    def set_like(self, post):
        if self.request.user != post.author:
            if self.request.user in post.likes.all():
                post.likes.remove(self.request.user)
            else:
                post.likes.add(self.request.user)
                post.save()
