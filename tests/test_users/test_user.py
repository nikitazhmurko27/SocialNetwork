import pytest
from django.urls import reverse

pytestmark = pytest.mark.django_db


class TestUserEndpoints:

    user_create_endpoint = reverse("user_create")
    user_login_endpoint = reverse("token_obtain_pair")

    @pytest.mark.parametrize(
        "email, username, password, status_code",
        [
            ("userexample.com", "testname", "123", 400),
            ("user@example.com", "testname", "", 400),
            ("test@test.com", "testname", "Test123123!!", 201),
        ],
    )
    def test_user_registration_data_validation(
        self, email, username, password, status_code, api_client
    ):
        data = {"email": email, "username": username, "password": password}
        response = api_client.post(self.user_create_endpoint, data=data)
        assert response.status_code == status_code

    @pytest.mark.django_db
    def test_user_login(self, default_user_data, api_client):
        response_reg = api_client.post(
            self.user_create_endpoint, data=default_user_data
        )
        assert response_reg.status_code == 201
        data = {
            "username": default_user_data["username"],
            "password": default_user_data["password"],
        }
        response_log = api_client.post(self.user_login_endpoint, data=data)
        assert response_log.status_code == 200
