from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token  # To handle token creation



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField()

    class Meta:
        model = get_user_model()  # Use the custom or default user model
        fields = ('username', 'email', 'password')  # Define fields to expose

    def create(self, validated_data):
        # Use the create_user method to create the user (this handles password hashing)
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        
        # Create a token for the newly created user
        Token.objects.create(user=user)
        
        return user
