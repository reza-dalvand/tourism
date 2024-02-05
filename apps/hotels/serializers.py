from rest_framework import serializers

from apps.hotels.models import Hotel, HotelAddress, Reservation, Room


class HotelAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelAddress
        fields = "__all__"


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class HotelSerializer(serializers.ModelSerializer):
    addresses = HotelAddressSerializer(read_only=True, many=True)
    rooms = RoomSerializer(read_only=True, many=True)

    class Meta:
        model = Hotel
        fields = "__all__"


class HotelReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"
