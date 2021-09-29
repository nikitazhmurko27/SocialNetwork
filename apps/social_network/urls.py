from django.urls import include, path
from rest_framework import routers

from apps.social_network.views import PostList

router = routers.DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("posts/", PostList.as_view(), name="posts_list"),
]
