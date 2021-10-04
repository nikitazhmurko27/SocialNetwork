from django.contrib.auth.models import User


class UserModelService:
    def __init__(self, validated_data):
        self.validated_data = validated_data

    def create(self):
        user = User(
            email=self.validated_data["email"],
            username=self.validated_data["username"],
        )
        user.set_password(self.validated_data["password"])
        user.save()
        return user
