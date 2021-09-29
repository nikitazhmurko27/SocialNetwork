from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts",
    )
    likes = models.ManyToManyField(User, through="PostAuthorLike")

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class PostAuthorLike(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="post_users"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
