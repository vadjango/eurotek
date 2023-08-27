import pytest
from report.models import DayReport
from .user import user
from datetime import datetime, timedelta


@pytest.fixture
def day_report(db, user) -> DayReport:
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
    return DayReport.objects.create(**report_data)
