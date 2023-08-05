from rest_framework.routers import SimpleRouter
from report.auth.register.viewsets import RegisterViewSet
from report.auth.codes.viewsets import VerificationView, LoginVerificationView
from report.auth.login.viewsets import LoginView
from django.urls import path


router = SimpleRouter()

router.register(r'auth/register', RegisterViewSet, "auth-register")

urlpatterns = [
    *router.urls,
    path("auth/login/", LoginView.as_view(), name="auth-login"),
    path("auth/verify/", VerificationView.as_view(), name='auth-verify'),
    path("auth/login-verify/", LoginVerificationView.as_view(), name="auth-login-verify")
    # re_path(r"^auth/2fa/", include('trench.urls')),
    # re_path(r"^auth/2fa/", include('trench.urls.jwt')),
]
