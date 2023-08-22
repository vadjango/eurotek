import logging
from .models import DayReport
from rest_framework import serializers

logger = logging.getLogger(__name__)


class DayReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DayReport
        fields = ["public_id", "employee", "shift", "start_date", "start_time", "end_time", "type_num", "operation_num",
                  "operation_name", "total_number_of_pieces", "min_norm", "total_hours", "created_at", "edited_at"]
        read_only_fields = ["public_id", "created_at", "edited_at"]
