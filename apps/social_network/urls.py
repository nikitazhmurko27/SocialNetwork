from django.urls import include, path
from rest_framework import routers

from apps.social_network.views import PostLike, PostList

router = routers.DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("posts/", PostList.as_view(), name="posts_list"),
    path("posts/<int:pk>/like", PostLike.as_view(), name="post_like"),
]
