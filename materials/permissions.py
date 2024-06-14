from rest_framework.permissions import BasePermission


class IsModerator(BasePermission):
    """Класс проверки на модератор"""
    message = "У вас нет прав, доступно только модераторам!"

    def has_permission(self, request, view):
        if request.user.groups.filter(name="moderator").exists():
            return True
        return False


class IsOwner(BasePermission):
    """Класс проверки на владельца"""
    message = "У вас нет прав, доступно только владельцу!"

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False
