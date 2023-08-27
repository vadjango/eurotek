import pytest
from report.fixtures.user import user
from report.fixtures.day_report import day_report
from report.notifications.models import Comment


@pytest.fixture
def comment(db, user, day_report) -> Comment:
    comment_data = {
        "day_report": day_report,
        "body": "Test body"
    }
    return Comment.objects.create(**comment_data)
