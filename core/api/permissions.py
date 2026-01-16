from rest_framework.permissions import BasePermission


class IsAdminOrManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in [
            "admin",
            "manager",
        ]


class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.role == "admin":
            return True
        return obj.owner == request.user


class IsLeadOwnerOrManager(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.role in ["admin", "manager"]:
            return True
        return obj.assigned_to == request.user


class IsDealOwnerOrManager(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.role in ["admin", "manager"]:
            return True
        return obj.owner == request.user
