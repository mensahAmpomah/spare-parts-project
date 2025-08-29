from rest_framework import serializers
from .models import User, UserProfile

# User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "firstname", "lastname", "username", "phone_number"]

# UserProfile model
class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Nested user info

    class Meta:
        model = UserProfile
        fields = ["id", "user", "profile_picture", "city", "created_at", "modified_at"]