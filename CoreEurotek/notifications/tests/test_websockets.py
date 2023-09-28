import pytest
import asyncio
from channels.testing import WebsocketCommunicator
from notifications.consumers import NotificationConsumer
from report.fixtures.user import user
from report.fixtures.day_report import day_report
from report.fixtures.comment import comment
from rest_framework_simplejwt.tokens import AccessToken

# TODO: test websocket


@pytest.mark.asyncio
async def test_websocket(user, day_report, comment):
    access_token = AccessToken.for_user(user)
    print(access_token)
    communicator = WebsocketCommunicator(NotificationConsumer.as_asgi(), f"notification-service?token={access_token}")
    communicator.scope["user"] = user.pk
    connected, subprotocol = await communicator.connect()
    assert connected
    await communicator.send_to(text_data="Olovo")
    response = await communicator.receive_json_from()

