from django.shortcuts import render
from .models import CustomUser
from .serializers import UserSerializers
from rest_framework import viewsets
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset=CustomUser.objects.all()
    serializer_class=UserSerializers

    