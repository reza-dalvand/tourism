from django.contrib import admin

from apps.users.models import User


class UserAdmin(admin.ModelAdmin):
    readonly_fields = ("password",)
    users_db = "users_db"

    def save_model(self, request, obj, form, change):
        # Tell Django to save objects to the 'users_db' database.
        obj.save(using=self.users_db)

    def delete_model(self, request, obj):
        # Tell Django to delete objects from the 'users_db' database
        obj.delete(using=self.users_db)

    def get_queryset(self, request):
        # Tell Django to look for objects on the 'users_db' database.
        return super().get_queryset(request).using(self.users_db)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Tell Django to populate ForeignKey widgets using a query
        # on the 'users_db' database.
        return super().formfield_for_foreignkey(db_field, request, using=self.users_db, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        # Tell Django to populate ManyToMany widgets using a query
        # on the 'users_db' database.
        return super().formfield_for_manytomany(db_field, request, using=self.users_db, **kwargs)


# Create separate admin for users
admin.site.register(User, UserAdmin)
