from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxLengthValidator, validate_comma_separated_integer_list
import uuid


class Shift(models.TextChoices):
    MORNING = "morning", _("Morning")
    AFTERNOON = "afternoon", _("Afternoon")
    NIGHT = "night", _("Night")


class DayReport(models.Model):
    public_uuid = models.UUIDField(db_index=True, default=uuid.uuid4, unique=True, editable=False)
    employee = models.ForeignKey(to=get_user_model(), on_delete=models.PROTECT)
    shift = models.CharField(choices=Shift.choices)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    type_num = models.CharField(max_length=4)
    operation_num = models.CharField(validators=[validate_comma_separated_integer_list])
    operation_name = models.CharField()
    total_number_of_pieces = models.IntegerField()
    min_norm = models.IntegerField()
    total_hours = models.FloatField()

    def __str__(self):
        return f"{self.employee}, {self.shift}, {self.date}"

    class Meta:
        constraints = [
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_shift_valid",
                check=models.Q(shift__in=Shift.values)
            )
        ]

