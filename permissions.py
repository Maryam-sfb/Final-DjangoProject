from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    message = "permission denied. You are not the owner of the object!"

    def has_object_permission(self, request, view, obj):   # obj is the question object
        if request.method in SAFE_METHODS:    # if the method is GET, HEAD or OPTIONS, let the user read the information
            return True
        return obj.user == request.user   # if the owner of object is the authenticated user, return True



