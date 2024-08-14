from rest_framework import permissions


class AuthenticatedReadOnlyAndStaffFullAccess(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or (request.user.is_authenticated and request.method in permissions.SAFE_METHODS)
