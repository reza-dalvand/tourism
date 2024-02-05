from rest_framework import serializers

from apps.hotels.models import Hotel, Reservation, Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class HotelSerializer(serializers.ModelSerializer):
    rooms = RoomSerializer(read_only=True, many=True)

    class Meta:
        model = Hotel
        fields = "__all__"


class HotelReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"
