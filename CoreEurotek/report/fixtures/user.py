import pytest
from report.auth.user.models import User

user_data = {
    "employee_id": 10254,
    "first_name": "David",
    "last_name": "Backhem",
    "password": "azxcA231&asd",
    "phone_number": "+380506442518",
}

additional_user_data = {
    "employee_id": 10255,
    "first_name": "Darid",
    "last_name": "Sickach",
    "password": "azxcA231&asd",
    "phone_number": "+380501252518",
}

manager_data = {
    "employee_id": 10256,
    "first_name": "Darid",
    "last_name": "Sickach",
    "password": "azxcA231&asd",
    "phone_number": "+380501252518",
}


@pytest.fixture
def user(db) -> User:
    return User.objects.create_user(**user_data)


@pytest.fixture
def additional_user(db) -> User:
    return User.objects.create_user(**additional_user_data)


@pytest.fixture
def manager(db) -> User:
    return User.objects.create_manager(**manager_data)
