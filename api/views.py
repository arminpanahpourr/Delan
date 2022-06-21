from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import User
from .serializers import UserSerializer


class Logout(APIView):
    """
    Delete user's authtoken
    """
    permission_classes = (AllowAny,)

    def post(self, request):
        request.user.auth_token.delete()
        return Response(data={'message': f'Bye {request.user.username}!'},
                        status=status.HTTP_204_NO_CONTENT)


class Register(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
