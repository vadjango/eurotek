import os
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from twilio.rest import Client


class RegisterVerificationView(APIView):
    @staticmethod
    def post(request, *args, **kwargs):
        print(request.data.get("phone_number"))
        phone_number = request.data.get("phone_number")
        request.session["phone_number"] = phone_number
        verification = Client().verify.v2.services(os.environ.get("TWILIO_VERIFY_SID")) \
            .verifications \
            .create(to=phone_number, channel="sms")
        return Response({"status": verification.status}, status=status.HTTP_200_OK)