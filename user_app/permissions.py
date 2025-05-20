from rest_framework.permissions import BasePermission

class IsAdminOrSuperAdmin(BasePermission):
    """
    Allows access only to users with role 'Admin' or 'SuperAdmin'.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in [1,2]
