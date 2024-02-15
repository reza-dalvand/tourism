from django.contrib import admin

from apps.hotels.models import Hotel, HotelAddress, Reservation, Room

# Register your models here.
admin.site.register(HotelAddress)
admin.site.register(Hotel)
admin.site.register(Reservation)
admin.site.register(Room)
