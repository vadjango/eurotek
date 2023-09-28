import os
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from twilio.rest import Client


class LoginVerificationView(APIView):
    @staticmethod
    def post(request, *args, **kwargs):
        data = {"user": request.session["user"]}
        data.update(request.session["auth"])
        phone_number = request.session.get("phone_number")
        otp_code = request.data.get("otp_code")
        test_otp = request.session.get("test_otp")
        # try:
        #     verification_check = Client().verify.v2.services(os.environ.get("TWILIO_VERIFY_SID")) \
        #         .verification_checks \
        #         .create(to=phone_number, code=otp_code)
        # except TwilioRestException:
        #     return Response(data={"error": "Cannot validate this number."},
        #                     status=status.HTTP_400_BAD_REQUEST)
        # if verification_check.status != "approved":
        if otp_code != test_otp:
            return Response({"error": "Code is expired or isn't valid!"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data=data, status=status.HTTP_200_OK)