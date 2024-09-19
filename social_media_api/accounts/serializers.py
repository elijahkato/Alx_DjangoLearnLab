from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'bio', 'profile_picture', 'followers')
        extra_kwargs = {
            'followers': {'required': False},  # Make followers optional
        }

    def create(self, validated_data):
        if 'followers' in validated_data:
            validated_data.pop('followers')
        return super().create(validated_data)