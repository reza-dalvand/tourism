from django.contrib import admin

from apps.users.models import User


class UserAdmin(admin.ModelAdmin):
    readonly_fields = ("password",)

    # def save_model(self, request, obj, form, change):
    #     # obj.set_password(form.cleaned_data["password"])
    #     return super().save_model(request, obj, form, change)
    #


# Register your models here.
admin.site.register(User, UserAdmin)
