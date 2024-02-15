from django.contrib import admin

from apps.tours.models import Tour, TourismCompany, TourismCompanyAddress, TourReservation

# Register your models here.
admin.site.register(TourismCompanyAddress)
admin.site.register(TourismCompany)
admin.site.register(TourReservation)
admin.site.register(Tour)
