from django.contrib.auth import login, logout
from rest_framework import status
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication

from ..serializer import LoginSerializer, UserSerializer


class UserView(APIView):

    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class LoginView(APIView):

    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)
    
    def post(self, request):
        serializer = LoginSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            user = serializer.validated_data
            login(request, user)
            return Response({"logged in"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class LogoutView(APIView):

    def get(self, request):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)