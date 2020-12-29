from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User

from accounts.serializers import UserSerializer


class UserCreate(generics.CreateAPIView):
    permission_classes = (AllowAny, )
    queryset = User.objects.all()
    serializer_class = UserSerializer
