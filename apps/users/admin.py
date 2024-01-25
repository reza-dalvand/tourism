from django.contrib import admin

from apps.users.models import User


class UserAdmin(admin.ModelAdmin):
    readonly_fields = ("password",)
    using = "users_db"


admin.site.register(User, UserAdmin)
