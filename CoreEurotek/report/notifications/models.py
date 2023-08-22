from django.db import models
from report.models import DayReport
from report.abstract.models import AbstractModel


class Comment(AbstractModel):
    day_report = models.ForeignKey(to=DayReport, on_delete=models.CASCADE, to_field="public_id")
    body = models.CharField(max_length=500)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.day_report}, comment_body: {self.body}"
