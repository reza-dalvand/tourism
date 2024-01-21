from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from apps.common.regex_patterns import MOBILE_PATTERN

mobile_number_field = serializers.CharField(
    max_length=11,
    validators=[RegexValidator(regex=MOBILE_PATTERN, message=_("Enter a valid mobile number"), code="Invalid Number")],
)


# I don't use model serializer to prevent checking unique validation
# for users already created but have not activating.
class LoginOrRegisterSerializer(serializers.Serializer):
    mobile = mobile_number_field


class VerifyOtpSerializer(serializers.Serializer):
    mobile = mobile_number_field
    code = serializers.IntegerField()


class CheckEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
