from rest_framework.permissions import BasePermission
from django.utils.translation import gettext_lazy as _

from users.models import UserRoles


class IsModerator(BasePermission):
    message = _('You are not a moderator')

    def has_permission(self, request, view):
        return request.user.role == UserRoles.MODERATOR


class IsSuperuser(BasePermission):
    message = _('You are not a Superuser')

    def has_permission(self, request, view):
        return request.user.is_superuser
