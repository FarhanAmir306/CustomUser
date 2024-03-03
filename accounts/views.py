from django.shortcuts import render
from .models import CustomUser
from .serializers import UserSerializers,LoginSerializer
from rest_framework import viewsets
from django.contrib.auth import login ,logout
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .serializers import LoginSerializer

# Create your views here.

# class UserViewSet(viewsets.ModelViewSet):
#     queryset=CustomUser.objects.all()
#     serializer_class=UserSerializers



class RegisterView(APIView):
    serializer_class = UserSerializers

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user_data = serializer.validated_data
            email=user_data.pop('email')
            password = user_data.pop('password')
            confirm_password = user_data.pop('confirm_password')
            if password != confirm_password:
                return Response({'error': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)
            
            # Ensure 'email' is passed only once when creating the user
            user = CustomUser.objects.create_user(email, password, **user_data)
            
            # Generate token for the user
            token, created = Token.objects.get_or_create(user=user)
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    serializer_class=LoginSerializer
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            print(user)
            login(request,user)
            # token, created = Token.objects.get_or_create(user=user)
            # return Response({'token': token.key}, status=status.HTTP_200_OK)
            return Response('login Successfull !')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogoutViewSet(APIView):
    def get(self, request, *args, **kwargs):
        if request.user:
            user_token=Token.objects.filter(user=request.user)
            user_token.delete()
            # logout(request)
        return Response({'detail': 'Logout successful'},status=status.HTTP_200_OK)