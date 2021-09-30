import pytest
from django.urls import reverse


@pytest.mark.django_db
@pytest.mark.parametrize(
    "email, username, password, status_code",
    [
        ("userexample.com", "testname", "123", 400),
        ("user@example.com", "testname", "", 400),
        ("test@test.com", "testname", "Test123123!!", 201),
    ],
)
def test_user_registration_data_validation(
    email, username, password, status_code, api_client
):
    url = reverse("user_create")
    data = {"email": email, "username": username, "password": password}
    response = api_client().post(url, data=data)
    assert response.status_code == status_code


@pytest.mark.django_db
def test_user_login(default_user_data, api_client):
    reg_url = reverse("user_create")
    response_reg = api_client().post(reg_url, data=default_user_data)
    assert response_reg.status_code == 201

    log_url = reverse("token_obtain_pair")
    data = {
        "username": default_user_data["username"],
        "password": default_user_data["password"],
    }
    response_log = api_client().post(log_url, data=data)
    assert response_log.status_code == 200
