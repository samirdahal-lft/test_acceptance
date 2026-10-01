from app import greeting


def test_greeting_non_empty_name():
    assert greeting("Alice") == "Good day, Alice"
