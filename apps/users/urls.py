from django.urls import path
from rest_framework import routers

from apps.users.views import UserCreate

router = routers.DefaultRouter()

urlpatterns = [
    path("", UserCreate.as_view(), name="user_create"),
]
