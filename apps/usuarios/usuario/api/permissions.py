from rest_framework.permissions import BasePermission

class IsUsuarioReadOnly(BasePermission):


    def has_permission(self, request, view):

        user_role = getattr(request.user.fk_id_rol, 'nombre', None)

        if user_role == "administrador":
            return True
        elif user_role == "instructor":
            return True
        elif user_role == "pasante":
            return request.method in ["GET", "POST"]
        elif user_role == "aprendiz":
            return request.method == "GET", "POST"
        else:
            return False
