from report.comment.models import Comment
from report.fixtures.user import user
from report.fixtures.day_report import day_report


def test_comment_create(db, user, day_report):
    comment_data = {
        "day_report": day_report,
        "body": "Test body"
    }
    comment = Comment.objects.create(**comment_data)
    assert comment.day_report == comment_data["day_report"]
    assert comment.body == comment_data["body"]
