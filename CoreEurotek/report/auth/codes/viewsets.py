import os

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

verify_sid = os.environ.get("TWILIO_VERIFY_SID")
client = Client()


class VerificationView(APIView):
    http_method_names = ["post"]

    @staticmethod
    def post(request, *args, **kwargs):
        phone_number = request.data["phone_number"]
        verification = client.verify.v2.services(verify_sid) \
            .verifications \
            .create(to=phone_number, channel="sms")
        return Response({"status": verification.status}, status=status.HTTP_200_OK)


class LoginVerificationView(APIView):

    @staticmethod
    def post(request, *args, **kwargs):
        otp_code = request.data["otp_code"]
        data = request.session["auth"]
        phone_number = request.session["phone_number"]
        try:
            verification_check = client.verify.v2.services(verify_sid) \
                .verification_checks \
                .create(to=phone_number, code=otp_code)
        except TwilioRestException:
            return Response(data={"error": "Cannot validate this number."},
                            status=status.HTTP_400_BAD_REQUEST)
        if verification_check.status != "approved":
            return Response({"error": "Code is expired or isn't valid!"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data=data, status=status.HTTP_200_OK)
