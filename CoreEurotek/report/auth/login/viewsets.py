import time

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.views import TokenObtainPairView
from report.tasks import get_otp_code
from twilio.base.exceptions import TwilioRestException
from report.auth.user.serializers import UserSerializer
import os
from twilio.rest import Client
from django.utils.translation import gettext_lazy as _

from report.auth.otp import generate_otp


class LoginView(TokenObtainPairView):
    http_method_names = ["post"]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        if "otp_code" not in request.data:
            # verification = Client().verify.v2.services(os.environ.get("TWILIO_VERIFY_SID")) \
            #     .verifications \
            #     .create(to=serializer.validated_data["user"].phone_number.as_e164, channel="sms")
            # return Response(data={"status": verification.status}, status=status.HTTP_200_OK)
            request.session["otp_code"] = get_otp_code()
            print(request.session["otp_code"])
            return Response(data={"status": "pending"}, status=status.HTTP_200_OK)
        # verification_check = Client().verify.v2.services(os.environ.get("TWILIO_VERIFY_SID")) \
        #     .verification_checks \
        #     .create(to=serializer.validated_data["user"].phone_number.as_e164, code=request.data["otp_code"])
        # if verification_check.status != "approved":
        #     return Response(data={"error": _("Otp code is invalid!")}, status=status.HTTP_400_BAD_REQUEST)
        del serializer.validated_data["user"]
        if request.data["otp_code"] != request.session["otp_code"]:
            return Response(data={"error": "Fuckoff"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data=serializer.validated_data, status=status.HTTP_200_OK)
