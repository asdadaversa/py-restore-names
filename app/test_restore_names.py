import pytest


@pytest.fixture()
def users() -> bool:
    return users == [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
    ]


def test_restore_names(users: list) -> None:
    for user in users:
        if "first_name" not in user or user["first_name"] is None:
            assert user["first_name"] == user["full_name"].split()[0]
