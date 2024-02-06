from rest_framework import serializers

from apps.tours.models import TourismCompany


class TourismCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = TourismCompany
        fields = "__all__"
