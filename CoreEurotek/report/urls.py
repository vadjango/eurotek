from rest_framework_nested import routers
from report.auth.register.viewsets import RegisterViewSet
from report.auth.register.views import RegisterVerificationView
from report.auth.login.views import LoginVerificationView
from report.auth.login.viewsets import LoginView
from rest_framework_simplejwt.views import TokenRefreshView
from .viewsets import DayReportViewSet
from django.urls import path
from notifications import consumers
from report.comment.viewsets import CommentViewSet


router = routers.SimpleRouter()

router.register('auth/register', RegisterViewSet, basename='auth-register')
router.register('report', DayReportViewSet, basename='report')

reports_router = routers.NestedSimpleRouter(parent_router=router, parent_prefix="report", lookup="report")
reports_router.register("comment", CommentViewSet, basename="report-comment")

urlpatterns = [
    path('auth/login/', LoginView.as_view(), name='auth-login'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='auth-refresh'),
    path('auth/register/verify/', RegisterVerificationView.as_view(), name='auth-verify'),
    path('auth/login/verify/', LoginVerificationView.as_view(), name='auth-login-verify'),
    *router.urls,
    *reports_router.urls
]

websocket_patterns = [
    path('notification-service', consumers.NotificationConsumer.as_asgi(), name='notification-service')
]
