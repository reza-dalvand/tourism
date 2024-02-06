from rest_framework.permissions import BasePermission


class CheckTourCompanyOwner(BasePermission):
    """checking a user want to change or create instance whether is owner?"""

    def has_permission(self, request, view):
        if request.method != "POST":
            return True
        elif request.method == "POST" and request.user.is_tour_company_owner:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in ["PUT", "PATCH", "DELETE"] and request.user == obj.owner:
            return True
        elif request.method == "GET":
            return True
        return False
