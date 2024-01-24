from django.contrib import admin

from apps.users.models import User


class UserAdmin(admin.ModelAdmin):
    readonly_fields = ("password",)
    using = "users_db"

    def save_model(self, request, obj, form, change):
        # Tell Django to save objects to the 'users_db' database.
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        # Tell Django to delete objects from the 'users_db' database
        obj.delete(using=self.using)

    def get_queryset(self, request):
        # Tell Django to look for objects on the 'users_db' database.
        return super().get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Tell Django to populate ForeignKey widgets using a query
        # on the 'users_db' database.
        return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        # Tell Django to populate ManyToMany widgets using a query
        # on the 'users_db' database.
        return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)


# Create separate admin for users
admin_users = admin.AdminSite("users_admin")
admin_users.register(User, UserAdmin)
