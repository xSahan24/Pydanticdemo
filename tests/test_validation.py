from app.models import User
import pytest
from pydantic import ValidationError

def test_valid_user():
    user = User(name="Alice", age=30, email="alice@example.com")
    assert user.name == "Alice"

def test_invalid_email():
    with pytest.raises(ValidationError):
        User(name="Bob", age=25, email="not-an-email")

def test_negative_age():
    with pytest.raises(ValidationError):
        User(name="Charlie", age=-5, email="charlie@example.com")
