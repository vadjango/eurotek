from channels.generic.websocket import AsyncJsonWebsocketConsumer
import json
from channels.db import database_sync_to_async
from rest_framework.utils.serializer_helpers import ReturnList

from report.notifications.models import Comment
from report.notifications.serializers import CommentSerializer


@database_sync_to_async
def aget_serialized_unread_comments_for_user(employee_id) -> ReturnList:
    comments = Comment.objects.filter(day_report__employee_id=employee_id, is_read=False)
    serializer = CommentSerializer(comments, many=True)
    return serializer.data


class NotificationConsumer(AsyncJsonWebsocketConsumer):
    groups = ["general"]  # TODO: read about it

    async def connect(self):
        user_id = self.scope["user"]
        await self.channel_layer.group_add(f"{user_id}--client", self.channel_name)
        comments = await aget_serialized_unread_comments_for_user(employee_id=user_id)
        await self.channel_layer.send(self.channel_name, {
            "type": "notification.message",
            "data": comments
        })
        await self.accept()

    async def notification_message(self, event):
        await self.send_json(content={
            "data": event["data"]
        })
