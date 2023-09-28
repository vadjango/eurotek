"""
ASGI config for CoreEurotek project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from report.comment.middlewares import WebSocketNotificationMiddleware
from report import urls

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CoreEurotek.settings')

django_asgi_application = get_asgi_application()

application = ProtocolTypeRouter(
    {
        "http": django_asgi_application,
        "websocket": WebSocketNotificationMiddleware(URLRouter(urls.websocket_patterns))
    }
)
