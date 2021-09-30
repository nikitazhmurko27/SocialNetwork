from django.db.models import Count
from rest_framework import filters, generics, mixins
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.social_network.models import Post
from apps.social_network.serializers import PostSerializer
from apps.social_network.services import PostAuthorLikeModelService


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


class PostLike(APIView):
    def get_object(self, pk):
        return Post.objects.get(pk=pk)

    def patch(self, request, pk):
        post_object = self.get_object(pk)
        serializer = PostSerializer(
            post_object, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            service = PostAuthorLikeModelService(request)
            service.set_like(post_object)
            return Response(serializer.data)
        return Response("wrong parameters")
