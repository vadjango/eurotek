from rest_framework.permissions import BasePermission, SAFE_METHODS
from report.models import DayReport


class UserReportsPermission(BasePermission):
    def has_object_permission(self, request, view, obj: DayReport):
        if request.user == obj.employee:
            return True
        if request.user.is_superuser:
            return request.method in SAFE_METHODS
        return False
