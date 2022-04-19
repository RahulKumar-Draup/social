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

# admin, moderator and user can access to perform put and delete
# ---applies to post and user model (no anonymous user can delete or update)

class Writebymoderator(BasePermission):
    def has_permission(self, request, view):
        obj = Group.objects.all()
        user = request.user
        if request.method == 'GET':
            return True
        elif request.method == 'POST' or request.method == 'Put' or request.method == 'DELETE':
            for i in range(len(obj)):
                if obj[i].is_member == True:
                    return True
                elif obj[i].is_moderator == True:
                    return True
                elif user.is_superuser:
                    return True
        return False




