from app import greeting


def test_greeting_non_empty_name():
    assert greeting("Alice") == "Good day, Alice"


def test_greeting_empty_name_returns_none():
    assert greeting("") is None


def test_greeting_whitespace_name_returns_none():
    assert greeting("   ") is None
