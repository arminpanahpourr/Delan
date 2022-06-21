from django.shortcuts import render
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from accounts.models import User
from .serializers import UserSerializer

Login = obtain_auth_token


class Register(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
