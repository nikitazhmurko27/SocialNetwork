import pytest


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient

    return APIClient


@pytest.fixture
def default_user_data():
    return {
        "email": "test@test.com",
        "username": "testname",
        "password": "Test123123!!",
    }
