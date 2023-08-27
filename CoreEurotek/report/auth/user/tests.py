import pytest
from report.auth.user.models import User


@pytest.mark.django_db
def test_default_user():
    user_data = {
        "employee_id": 99999,
        "first_name": "test",
        "last_name": "supertest",
        "phone_number": "+380000000000",
        "password": "asdfg12312",
        "avatar": r"WIN_20230716_00_09_04_Pro.jpg"
    }
    u = User.objects.create_user(**user_data)
    assert u.employee_id == user_data["employee_id"]
    assert u.first_name == user_data["first_name"]
    assert u.last_name == user_data["last_name"]
    assert u.phone_number == user_data["phone_number"]
    assert u.avatar == user_data["avatar"]
