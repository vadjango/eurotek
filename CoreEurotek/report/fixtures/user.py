import pytest
from report.auth.user.models import User

user_data = {
    "employee_id": 10254,
    "first_name": "David",
    "last_name": "Backhem",
    "password": "azxcA231&asd",
    "phone_number": "+380506442518",
}


@pytest.fixture
def user(db) -> User:
    return User.objects.create_user(**user_data)
