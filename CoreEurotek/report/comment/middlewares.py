from urllib.parse import parse_qs
from rest_framework_simplejwt.tokens import AccessToken, TokenError
from django.contrib.auth.models import AnonymousUser


class WebSocketNotificationMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        query_dict = parse_qs(scope["query_string"])
        token = query_dict[b"token"][0].decode("UTF-8")

        try:
            access_token = AccessToken(token)
            scope["user"] = access_token["user_id"]
            print(token)
        except TokenError:
            scope["user"] = AnonymousUser()

        return await self.app(scope, receive, send)
