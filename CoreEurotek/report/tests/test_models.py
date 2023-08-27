import pytest
from datetime import datetime, timedelta
from report.fixtures.user import user
from report.models import DayReport


@pytest.mark.django_db
def test_day_report_create(user):
    dt_tm = datetime.now()
    start_time = (dt_tm - timedelta(hours=8)).time()
    end_time = dt_tm.time()
    report_data = {
        "employee": user,
        "shift": "night",
        "start_date": dt_tm.strftime("%Y-%m-%d"),
        "start_time": start_time.strftime("%H:%M:%S"),
        "end_time": end_time.strftime("%H:%M:%S"),
        "type_num": "015",
        "operation_num": "125",
        "operation_name": "Some operation",
        "total_number_of_pieces": 2015,
        "min_norm": 500,
        "total_hours": 7.5
    }
    day_report = DayReport.objects.create(**report_data)
    assert day_report.employee == report_data["employee"]
    assert day_report.shift == report_data["shift"]
    assert day_report.start_date == report_data["start_date"]
    assert day_report.start_time == report_data["start_time"]
    assert day_report.start_time == report_data["start_time"]
    assert day_report.end_time == report_data["end_time"]
    assert day_report.type_num == report_data["type_num"]
    assert day_report.operation_num == report_data["operation_num"]
    assert day_report.operation_name == report_data["operation_name"]
    assert day_report.total_number_of_pieces == report_data["total_number_of_pieces"]
    assert day_report.min_norm == report_data["min_norm"]
    assert day_report.total_hours == report_data["total_hours"]

