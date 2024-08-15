from rest_framework import permissions


class AuthenticatedReadOnlyAndStaffFullAccess(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # allow all operations for staff, read only for authorized non staff, otherwise, forbid any.

        return request.user.is_staff or (request.user.is_authenticated and request.method in permissions.SAFE_METHODS)
