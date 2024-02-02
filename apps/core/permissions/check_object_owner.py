from rest_framework.permissions import BasePermission


class CheckObjectOwner(BasePermission):
    """allow to change object just by owner"""

    def has_object_permission(self, request, view, obj):
        if request.method in ["PUT", "PATCH", "DELETE"] and request.user == obj.owner:
            return True
        return False
