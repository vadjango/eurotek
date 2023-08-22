from rest_framework.response import Response
from .serializers import CommentSerializer
from report.auth.permissions import CommentUserPermission
from rest_framework import viewsets, status
from rest_framework.decorators import action
from report.notifications.models import Comment
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    http_method_names = ["get", "post", "patch", "put", "delete"]
    permission_classes = [CommentUserPermission]
    lookup_field = "public_id"
    channel_layer = get_channel_layer()

    @action(methods=["post"], detail=True)
    def read(self, request, *args, **kwargs):
        comment = self.get_object()
        comment.is_read = True
        comment.save()
        serializer = self.serializer_class()
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def get_queryset(self):
        if self.request.user.is_manager:
            return Comment.objects.all()
        return Comment.objects.filter(day_report__employee=self.request.user)

    def create(self, request, *args, **kwargs):
        data = {**request.data, "day_report": kwargs.get("report_public_id")}
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        self._send_notification(serializer.data)
        headers = self.get_success_headers(serializer.data)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def _send_notification(self, data):
        async_to_sync(self.channel_layer.group_send)(f'{data["day_report"]["employee"]}--client', {
            "type": "notification.message",
            "data": [data]
        })
