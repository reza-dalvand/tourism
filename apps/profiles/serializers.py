from django.contrib.auth import get_user_model
from rest_framework import serializers


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()


class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "email", "avatar", "age", "address"]
