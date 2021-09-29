from django.db.models import Count
from rest_framework import filters, generics, mixins

from apps.social_network.models import Post
from apps.social_network.serializers import PostSerializer


class PostList(
    mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
):

    serializer_class = PostSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ["-created_at"]

    def get_queryset(self):
        queryset = Post.objects.all()
        likes_count = self.request.query_params.get("likes_count")
        if likes_count is not None:
            queryset = queryset.annotate(c=Count("likes")).filter(
                c=likes_count
            )
        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
