from rest_framework import generics, mixins
from rest_framework.permissions import AllowAny

from apps.users.serializers import CreateUserSerializer


class UserCreate(mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = CreateUserSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
