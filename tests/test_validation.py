from app.models import User
import pytest
from pydantic import ValidationError

def test_valid_user():
    user = User(name="Sahan", age=19, email="Sahan@example.com")
    assert user.name == "Alice"

def test_invalid_email():
    with pytest.raises(ValidationError):
        User(name="Jasper", age=23, email="not-an-email")

def test_negative_age():
    with pytest.raises(ValidationError):
        User(name="Luis", age=-5, email="Luis@example.com")
