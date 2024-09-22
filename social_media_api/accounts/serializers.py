from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token  # To handle token creation

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Ensure password is write-only
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()  # Use the custom or default user model
        fields = ('id', 'username', 'email', 'bio', 'profile_picture', 'password', 'followers_count', 'following_count')
        extra_kwargs = {
            'password': {'write_only': True},  # Ensure password is not included in read responses
        }

    def get_followers_count(self, obj):
        return obj.followers.count()

    def get_following_count(self, obj):
        return obj.following.count()
    
    def create(self, validated_data):
        # Extract and remove the password from the validated data
        password = validated_data.pop('password')
        
        # Create a new user instance using the remaining validated data
        user = get_user_model().objects.create(**validated_data)
        
        # Set the user's password (this ensures it is hashed correctly)
        user.set_password(password)
        user.save()
        
        # Create a token for the newly created user
        Token.objects.create(user=user)
        
        return user
