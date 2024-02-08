from rest_framework import serializers

from apps.tours.models import Tour, TourismCompany, TourReservation


class TourismCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = TourismCompany
        fields = "__all__"


class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = "__all__"


class TourReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourReservation
        fields = "__all__"
