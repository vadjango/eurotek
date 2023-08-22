from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from report.auth.permissions import ReportUserPermission
from .serializers import DayReportSerializer
from .models import DayReport


class DayReportViewSet(viewsets.ModelViewSet):
    serializer_class = DayReportSerializer
    http_method_names = ["get", "post", "patch", "put"]
    permission_classes = [ReportUserPermission]
    lookup_field = "public_id"

    def get_queryset(self):
        if self.request.user.is_manager:
            return DayReport.objects.all()
        return DayReport.objects.filter(employee=self.request.user)

    def create(self, request, *args, **kwargs):
        data = {**request.data, "employee": request.user.pk}
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        data = {**request.data, "employee": request.user.pk}
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
