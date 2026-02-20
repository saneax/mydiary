import pytest
import sys
from mydiary.cli import main
from mydiary.db import init_db
import os

@pytest.fixture(autouse=True)
def setup_db(monkeypatch):
    test_db = "test_cli.db"
    monkeypatch.setattr("mydiary.db.DB_PATH", test_db)
    init_db()
    yield
    if os.path.exists(test_db):
        os.remove(test_db)

def test_cli_add(capsys, monkeypatch):
    monkeypatch.setattr(sys, "argv", ["mydiary", "add", "12345", "--name", "CLI User"])
    main()
    captured = capsys.readouterr()
    assert "Added: CLI User" in captured.out

def test_cli_list(capsys, monkeypatch):
    # First add a contact
    monkeypatch.setattr(sys, "argv", ["mydiary", "add", "999", "--name", "List User"])
    main()
    
    # Then list
    monkeypatch.setattr(sys, "argv", ["mydiary", "list"])
    main()
    captured = capsys.readouterr()
    assert "List User" in captured.out
    assert "999" in captured.out
