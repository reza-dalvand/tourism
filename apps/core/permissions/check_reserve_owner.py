from rest_framework.permissions import BasePermission


class CheckReserveOwner(BasePermission):
    """checking a user want to change reserve instance whether is owner that?"""

    def has_object_permission(self, request, view, obj):
        if request.method in ["PUT", "PATCH", "DELETE", "GET"] and request.user == obj.user:
            return True
        return False
