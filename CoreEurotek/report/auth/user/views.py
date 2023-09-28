from rest_framework import status
from rest_framework.response import Response
from report.auth.user.models import User
from rest_framework.views import APIView

class ValidateEmployeeIDView(APIView):
    http_method_names = ["post"]

    @staticmethod
    def post(request):
        employee_id = request.data["employee_id"]
        return Response(data=request.data, status=status.HTTP_200_OK)
