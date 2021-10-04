import pytest
from django.contrib.auth.models import User

from apps.social_network.models import Post


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient

    return APIClient()


@pytest.fixture
def default_user_data():
    return {
        "email": "lennon@thebeatles.com",
        "username": "john",
        "password": "Test123123!!",
    }


@pytest.fixture
def default_user():
    user = User.objects.create_user(
        "john", "lennon@thebeatles.com", "Test123123!!"
    )
    user.save()
    return user


@pytest.fixture
def test_post():
    user = User.objects.create_user(
        "john111", "lennon@thebeatles.com", "Test123123!!"
    )
    user.save()
    post = Post.objects.create(
        author=user, title="test title", content="test content"
    )
    return post


@pytest.fixture
def liked_post():
    user = User.objects.create_user(
        "john007", "lennon007@thebeatles.com", "Test123123!!"
    )
    user.save()
    post = Post.objects.create(
        author=user,
        title="test007",
        content="test content007",
    )
    post.likes.add(user)
    post.save()
    return post
