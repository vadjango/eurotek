from channels.generic.websocket import AsyncJsonWebsocketConsumer
import logging
from channels.db import database_sync_to_async
from rest_framework.utils.serializer_helpers import ReturnList

from report.notifications.models import Comment
from report.notifications.serializers import CommentSerializer

logger = logging.getLogger(__name__)


@database_sync_to_async
def aget_serialized_unread_comments_for_user(employee_id) -> ReturnList:
    comments = Comment.objects.filter(day_report__employee_id=employee_id, is_read=False)
    serializer = CommentSerializer(comments, many=True)
    return serializer.data


class NotificationConsumer(AsyncJsonWebsocketConsumer):
    groups = ["general"]  # TODO: read about it

    async def connect(self):
        await self.accept()
        user_id = self.scope["user"]
        print(f"User_id: {user_id}")
        await self.channel_layer.group_add(f"{user_id}--client", self.channel_name)
        comments = await aget_serialized_unread_comments_for_user(employee_id=user_id)
        for comm in comments:
            await self.channel_layer.send(self.channel_name, {
                "type": "notification.message",
                "info": f"The comment was created for the report {comm['day_report']['start_date']}",
                "link": f"http://127.0.0.1:8000/api/v1/report/{comm['day_report']['public_id']}/comment/{comm['public_id']}/"
            })

    async def notification_message(self, event):
        logger.warning("Message was sented!")
        data = {"info": event["info"]}
        if event.get("link"):
            data["link"] = event["link"]
        await self.send_json(content=data)
