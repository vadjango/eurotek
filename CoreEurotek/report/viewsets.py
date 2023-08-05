from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import DayReportSerializer
from .models import DayReport


class DayReportViewSet(viewsets.ModelViewSet):
    serializer_class = DayReportSerializer
    http_method_names = ["get", "post"]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return DayReport.objects.filter(employee=self.request.user)

    def create(self, request, *args, **kwargs):
        request.data["employee"] = request.user.pk
        return super().create(request, *args, **kwargs)
