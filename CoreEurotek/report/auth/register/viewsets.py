import os
from rest_framework import viewsets, status
from twilio.base.exceptions import TwilioRestException
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from twilio.rest import Client
from .serializers import RegisterSerializer, UserSerializer


class RegisterViewSet(viewsets.ModelViewSet):
    token_class = RefreshToken
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
    http_method_names = ["post"]
    verify_sid = os.environ.get("TWILIO_VERIFY_SID")

    def create(self, request, *args, **kwargs):
        otp_code = request.data["otp_code"]
        verified_number = request.data["phone_number"]
        reg_serializer = self.get_serializer(data=request.data)
        reg_serializer.is_valid(raise_exception=True)
        # client = Client()
        # try:
        #     verification_check = client.verify.v2.services(self.verify_sid) \
        #         .verification_checks \
        #         .create(to=verified_number, code=otp_code)
        # except TwilioRestException:
        #     return Response(data={"error": "Cannot validate this number."},
        #                     status=status.HTTP_400_BAD_REQUEST)
        # if verification_check.status != "approved":
        #     raise ValueError("Verification code is not valid")
        user = reg_serializer.save()
        refresh = self.token_class.for_user(user)
        data = {
            "access": str(refresh.access_token),
            "refresh": str(refresh)
        }
        return Response(data=data, status=status.HTTP_201_CREATED)
