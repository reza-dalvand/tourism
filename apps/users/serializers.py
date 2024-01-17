import logging

from django.core.validators import RegexValidator
from rest_framework import serializers

from apps.common.regex_patterns import PHONE_PATTERN
from apps.services.send_otp import send_sms
from apps.users.models import User
from apps.utils.generate_otp import generate_otp_code

logger = logging.getLogger("main")


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("phone",)

    def create(self, validate_data):
        user = User.objects.create(phone=validate_data["phone"])
        otp_code = generate_otp_code()
        try:
            user.otp = otp_code
            user.save()
            send_sms(user, otp_code)
        except Exception as e:
            logger.exception(e)
        return user


class VerifyRegistrationSerializer(serializers.Serializer):
    phone = serializers.CharField(
        max_length=11,
        validators=[RegexValidator(regex=PHONE_PATTERN, message="Enter a valid phone number", code="Invalid Number")],
    )
    code = serializers.IntegerField()


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
