from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # read permission to everyone (get, head, options)
        if request.method in permissions.SAFE_METHODS:
            return True

        # edit permissions only to owner
        return obj.owner == request.user
