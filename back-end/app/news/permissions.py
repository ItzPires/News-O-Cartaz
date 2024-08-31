from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Permissão que permite somente admins realizar ações de escrita (POST, PUT, DELETE),
    enquanto usuários normais só podem ler (GET).
    """

    def has_permission(self, request, view):
        # Se o método for seguro (GET, HEAD ou OPTIONS), permite sempre
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Se não for um método seguro, verifica se o usuário é admin
        return request.user and request.user.is_staff
