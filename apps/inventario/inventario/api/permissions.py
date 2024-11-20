from rest_framework.permissions import BasePermission

class Permiso(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        if request.method == 'POST':
            return True
        if request.method == 'DELETE':
            return True
        if request.method == 'PATCH':
            return True
        else:
            return request.user.is_staff
