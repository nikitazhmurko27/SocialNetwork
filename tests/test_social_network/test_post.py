import json

import pytest
from django.urls import reverse

from apps.social_network.models import Post

pytestmark = pytest.mark.django_db


class TestPostEndpoints:
    post_default_endpoint = reverse("posts_list")

    @pytest.mark.parametrize(
        "title, content, status_code",
        [
            ("", "test content", 400),
            ("test title", "", 400),
            ("test title", "test content", 201),
        ],
    )
    def test_posts_create(
        self, title, content, status_code, default_user, api_client
    ):
        api_client.force_authenticate(user=default_user)
        data = {"title": title, "content": content}
        response = api_client.post(self.post_default_endpoint, data=data)
        assert response.status_code == status_code

    @pytest.mark.parametrize(
        "title, post_content",
        [
            ("test title", "test content"),
        ],
    )
    def test_posts_get(self, title, post_content, default_user, api_client):
        api_client.force_authenticate(user=default_user)
        Post.objects.create(
            author=default_user, title=title, content=post_content
        )
        response = api_client.get(self.post_default_endpoint)
        content = json.loads(response.content)
        results = content["results"]
        assert response.status_code == 200
        assert content["count"] == 1
        assert results[0]["title"] == title
        assert results[0]["content"] == post_content

    def test_posts_get_by_like(self, liked_post, default_user, api_client):
        api_client.force_authenticate(user=default_user)
        response = api_client.get(
            f"{self.post_default_endpoint}?likes_count=1"
        )
        content = json.loads(response.content)
        results = content["results"]
        assert response.status_code == 200
        assert content["count"] == 1
        assert results[0]["title"] == liked_post.title
        assert results[0]["content"] == liked_post.content

    def test_posts_like(self, default_user, api_client, test_post):
        api_client.force_authenticate(user=default_user)
        # like
        response = api_client.patch(
            f"{self.post_default_endpoint}{test_post.pk}/like"
        )
        content = json.loads(response.content)
        assert response.status_code == 200
        assert len(content["likes"]) == 1
        # unlike
        response = api_client.patch(
            f"{self.post_default_endpoint}{test_post.pk}/like"
        )
        content = json.loads(response.content)
        assert response.status_code == 200
        assert len(content["likes"]) == 0

    def test_like_self_post(self, test_post, api_client):
        user = test_post.author
        api_client.force_authenticate(user=user)
        response = api_client.patch(
            f"{self.post_default_endpoint}{test_post.pk}/like"
        )
        content = json.loads(response.content)
        assert response.status_code == 200
        assert len(content["likes"]) == 0
