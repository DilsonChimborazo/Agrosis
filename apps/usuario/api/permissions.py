from rest_framework.permissions import BasePermission

class IsUsuarioReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET, POST":
            return True
        else:
            return request.user.is_staff