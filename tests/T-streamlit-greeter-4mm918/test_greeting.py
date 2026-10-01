from pathlib import Path

from app import greeting
from streamlit.testing.v1 import AppTest

_APP_PATH = Path(__file__).parents[2] / "app.py"


def test_greeting_non_empty_name():
    assert greeting("Alice") == "Good day, Alice"


def test_greeting_empty_name_returns_none():
    assert greeting("") is None


def test_greeting_whitespace_name_returns_none():
    assert greeting("   ") is None


def test_greeting_trims_surrounding_whitespace():
    assert greeting("  Alice  ") == "Good day, Alice"


def test_app_shows_greeting_when_name_entered():
    at = AppTest.from_file(_APP_PATH).run()
    at.text_input[0].set_value("Alice").run()
    assert any("Good day, Alice" in str(el.value) for el in at.markdown)


def test_app_shows_no_greeting_when_name_empty():
    at = AppTest.from_file(_APP_PATH).run()
    assert not at.markdown
