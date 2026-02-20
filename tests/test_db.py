import os
import pytest
from mydiary.db import init_db, add_contact

@pytest.fixture(autouse=True)
def setup_db():
    # Use a temporary database for testing
    test_db = "test_mydiary.db"
    import mydiary.db
    original_db = mydiary.db.DB_PATH
    mydiary.db.DB_PATH = test_db
    init_db()
    yield
    if os.path.exists(test_db):
        os.remove(test_db)
    mydiary.db.DB_PATH = original_db

def test_add_contact_basic():
    success, message = add_contact("1234567890", name="Test User", address="Test Address")
    assert success is True
    assert "Added: Test User" in message

def test_add_contact_only_phone():
    success, message = add_contact("1234567890")
    assert success is True
    assert "unknown_1" in message
    assert "unknown_address_1" in message

def test_unique_unknowns():
    add_contact("1")
    add_contact("2")
    success, message = add_contact("3")
    assert "unknown_3" in message
    assert "unknown_address_3" in message

def test_duplicate_name_error():
    add_contact("123", name="Duplicate")
    success, message = add_contact("456", name="Duplicate")
    assert success is False
    assert "UNIQUE constraint failed" in message
