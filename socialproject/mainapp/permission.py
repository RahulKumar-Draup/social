from rest_framework.permissions import BasePermission
from . models import *


# only admin can access to perform put and delete ---applies to group only
class Writebyadmin(BasePermission):
    def has_permission(self, request, view):
        print(request.user)
        user = request.user
        if request.method == 'GET':
            return True
        elif request.method == 'POST' or request.method == 'Put' or request.method == 'DELETE':
            if user.is_superuser:
                return True
        return False




