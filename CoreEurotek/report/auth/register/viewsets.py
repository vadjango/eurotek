from rest_framework import viewsets, status
from twilio.base.exceptions import TwilioRestException
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from twilio.rest import Client
import os
from .serializers import UserSerializer


class RegisterViewSet(viewsets.ModelViewSet):
    token_class = RefreshToken
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    http_method_names = ["post"]
    verify_sid = os.environ.get("TWILIO_VERIFY_SID")

    def create(self, request, *args, **kwargs):
        otp_code = request.data["otp_code"]
        verified_number = request.data["phone_number"]
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        client = Client()
        try:
            verification_check = client.verify.v2.services(self.verify_sid) \
                .verification_checks \
                .create(to=verified_number, code=otp_code)
        except TwilioRestException:
            return Response(data={"error": "Cannot validate this number. Check if you didn't change a number!"},
                            status=status.HTTP_400_BAD_REQUEST)
        if verification_check.status != "approved":
            raise ValueError("Verification code is not valid")
        serializer.create(serializer.validated_data)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
