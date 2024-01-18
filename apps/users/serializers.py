import logging

from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from apps.common.regex_patterns import MOBILE_PATTERN
from apps.users.models import User

logger = logging.getLogger("main")

mobile_number_field = serializers.CharField(
    max_length=11,
    validators=[RegexValidator(regex=MOBILE_PATTERN, message=_("Enter a valid mobile number"), code="Invalid Number")],
)


class RegisterSerializer(serializers.Serializer):
    mobile = mobile_number_field


class VerifyRegistrationSerializer(serializers.Serializer):
    mobile = mobile_number_field
    code = serializers.IntegerField()


class LoginSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=11, min_length=11)
    password = serializers.CharField(max_length=256, write_only=True)

    def validate(self, validated_data):
        mobile_number = validated_data["mobile"]
        password = validated_data["password"]
        user = User.objects.get(mobile__iexact=mobile_number)
        if not user or not user.check_password(password):
            raise serializers.ValidationError({"error": "mobile number or password is incorrect"})
        return validated_data
