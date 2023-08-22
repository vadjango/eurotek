from rest_framework import serializers
from .models import Comment
from report.serializers import DayReportSerializer


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["public_id", "day_report", "body", "is_read", "created_at", "edited_at"]
        read_only_fields = ["public_id", "created_at", "edited_at"]

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["day_report"] = DayReportSerializer(instance.day_report).data
        return rep
