from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.views import TokenObtainPairView
import os
from twilio.rest import Client


class LoginView(TokenObtainPairView):
    http_method_names = ["post"]
    verify_sid = os.environ.get("TWILIO_VERIFY_SID")

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        request.session["auth"] = serializer.validated_data
        phone_number = serializer.user.phone_number
        request.session["phone_number"] = phone_number.as_e164
        client = Client()
        verification = client.verify.v2.services(self.verify_sid) \
            .verifications \
            .create(to=phone_number.as_e164, channel="sms")
        return Response(data={"status": verification.status}, status=status.HTTP_200_OK)
