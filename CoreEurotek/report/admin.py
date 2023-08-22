from django.contrib import admin
from .models import DayReport


class DayReportAdmin(admin.ModelAdmin):
    list_display = ("employee", "shift", "start_date")


admin.site.register(DayReport, DayReportAdmin)
