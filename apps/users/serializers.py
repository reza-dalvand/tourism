from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from apps.users.models import User


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("phone", "email", "password", "password2")
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, validated_data):
        password = validated_data.get("password")
        password2 = validated_data.get("password2")
        if password != password2:
            raise serializers.ValidationError({"error": _("passwords not match")})
        return validated_data

    def create(self, validate_data):
        user = User.objects.create(phone=validate_data["phone"], email=validate_data["email"])
        user.set_password(validate_data["password"])

        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=11, min_length=11)
    password = serializers.CharField(max_length=256, write_only=True)

    def validate(self, validated_data):
        phone_number = validated_data["phone"]
        password = validated_data["password"]
        user = User.objects.get(phone__iexact=phone_number)
        if not user or not user.check_password(password):
            raise serializers.ValidationError({"error": "phone number or password is incorrect"})
        return validated_data
