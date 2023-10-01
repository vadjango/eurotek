import os
from rest_framework.decorators import action
from rest_framework import viewsets, status
from twilio.base.exceptions import TwilioRestException
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from twilio.rest import Client
from .serializers import RegisterSerializer
from report.auth.otp import generate_otp
from ...tasks import get_otp_code


class RegisterViewSet(viewsets.ModelViewSet):
    token_class = RefreshToken
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
    http_method_names = ["post"]

    @action(methods=["post"], detail=False)
    def validate_fields(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        errors = {}
        for key in request.data.keys():
            if key in serializer.errors:
                errors[key] = serializer.errors[key]
        if errors:
            return Response(data=errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if "otp_code" not in request.data:
            # verification = Client().verify.v2.services(os.environ.get("TWILIO_VERIFY_SID")) \
            #         .verifications.create(to=request.data["phone_number"], channel="sms")
            request.session["otp_code"] = get_otp_code()
            print(request.session["otp_code"])
            return Response(data={"status": "pending"}, status=status.HTTP_200_OK)
        # try:
        #     verification_check = Client().verify.v2.services(os.environ.get("TWILIO_VERIFY_SID")) \
        #         .verification_checks \
        #         .create(to=request.data["phone_number"], code=request.data["otp_code"])
        # except TwilioRestException as e:
        #     return Response(data={"error": str(e)},
        #                     status=status.HTTP_400_BAD_REQUEST)
        # if verification_check.status != "approved":
        if request.data["otp_code"] != request.session["otp_code"]:
            return Response({"error": "Verification code is not valid!"}, status=status.HTTP_400_BAD_REQUEST)
        user = serializer.save()
        refresh = self.token_class.for_user(user)
        data = {
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "user": serializer.data
        }
        return Response(data=data, status=status.HTTP_201_CREATED)
