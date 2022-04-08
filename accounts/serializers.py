from .models import CustomUser
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer

class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['email', 'id']
        extra_kwargs = { 
            'email': {'validators': []}
            }

class CustomUserRegisterSerializer(RegisterSerializer):
    username = None

    def get_cleaned_data(self):
        return {
            "password1": self.validated_data.get("password1", ""),
            "email": self.validated_data.get("email", "")
        }