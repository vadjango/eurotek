from rest_framework.permissions import IsAuthenticated, SAFE_METHODS


class ReportUserPermission(IsAuthenticated):
    """
    Permission which should be used in ReportViewSet
    """
    def has_object_permission(self, request, view, obj):
        if request.user == obj.employee or request.user.is_manager:
            return True
        return False


class CommentUserPermission(IsAuthenticated):
    """
    Permission which should be used in CommentViewSet
    """

    def has_permission(self, request, view):
        if not super().has_permission(request, view):
            return False
        if request.user.is_manager:
            return True
        last_path = str(request).split("/")[-2]
        if last_path in ["read"] and request.method in ["POST"]:
            return True
        return request.method in SAFE_METHODS
