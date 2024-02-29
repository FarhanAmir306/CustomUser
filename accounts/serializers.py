from rest_framework import serializers
from .models import CustomUser

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=('first_name','last_name','email','password','confirm_password','phone','avatar','address',)


