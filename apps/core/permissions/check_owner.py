from rest_framework.permissions import BasePermission


class CheckOwner(BasePermission):
    """allow to change or create instance by owners"""

    def has_object_permission(self, request, view, obj):
        if request.method is "POST" and request.user.is_hotel_owner:
            return True
        elif request.method in ["PUT", "PATCH", "DELETE"] and request.user == obj.owner:
            return True
        return False
