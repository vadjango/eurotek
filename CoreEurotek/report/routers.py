from rest_framework.routers import SimpleRouter
from report.auth.register.viewsets import RegisterViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from django.urls import path

router = SimpleRouter()

router.register(r'auth/register', RegisterViewSet, "auth-register")

urlpatterns = [
    *router.urls,
    path("auth/login/", TokenObtainPairView.as_view(), name="auth-login")
]
