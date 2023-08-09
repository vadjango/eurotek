from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from rest_framework import status
from django.core.exceptions import ValidationError
from rest_framework.response import Response
from report.auth.permissions import UserReportsPermission
from .serializers import DayReportSerializer
from .models import DayReport


class DayReportViewSet(viewsets.ModelViewSet):
    serializer_class = DayReportSerializer
    http_method_names = ["get", "post", "patch", "put"]
    permission_classes = [UserReportsPermission]
    lookup_field = "public_uuid"

    def get_queryset(self):
        if self.request.user.is_superuser is True:
            return DayReport.objects.all()
        return DayReport.objects.filter(employee=self.request.user)

    def create(self, request, *args, **kwargs):
        request.data["employee"] = request.user.pk
        return super().create(request, *args, **kwargs)
        # TODO: add constraint by (employee, date) or (employee, date, start_time, end_time)
