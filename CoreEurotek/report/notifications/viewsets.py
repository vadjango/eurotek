from django.http import Http404
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
    http_method_names = ["get", "post", "delete"]
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
        report_public_id = self.kwargs.get("report_public_id")
        if report_public_id is None:
            raise Http404
        return Comment.objects.filter(day_report__public_id=report_public_id,
                                      day_report__employee=self.request.user)

    def create(self, request, *args, **kwargs):
        data = {**request.data, "day_report": kwargs.get("report_public_id")}
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        self._send_notification({
            "to": serializer.data["day_report"]["employee"],
            "info": f"The comment was created for the report {serializer.data['day_report']['start_date']}",
            "link": f"http://127.0.0.1:8000/api/v1/report/{serializer.data['day_report']['public_id']}/comment/{serializer.data['public_id']}/"
        })
        headers = self.get_success_headers(serializer.data)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self._send_notification({
            "to": instance.day_report.employee_id,
            "info": f"The comment for the report {instance.day_report.start_date} was deleted"
        })
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def _send_notification(self, data):
        async_to_sync(self.channel_layer.group_send)(f'{data["to"]}--client', {
            "type": "notification.message",
            "info": data.get("info"),
            "link": data.get("link")
        })
