import pytest
from report.fixtures.day_report import day_report
from report.fixtures.user import user


@pytest.mark.django_db
def test_day_report(day_report):
    assert day_report.shift == "night"
