"""Test for String Repeat."""


import pytest


STRING_REPEAT_TABLE = [
                      [4, "hi ", "hi hi hi hi "],
                      [3, "thank ", "thank thank thank "],
                      [2, "you ", "you you "],
                      [5, "gabe ", "gabe gabe gabe gabe gabe "]]


@pytest.mark.parametrize("n, m, result", STRING_REPEAT_TABLE)
def test_rrepeat_str(n, m, result):
    """Test to verify function works."""
    from string_repeat import repeat_str
    assert repeat_str(n, m) == result
