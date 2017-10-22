"""Test for Reverse List."""


import pytest


REVERSE_TABLE = [
                ["hello", "olleh"],
                ["thank", "knaht"],
                ["you", "uoy"],
                ["gabe", "ebag"]]


@pytest.mark.parametrize("n, result", REVERSE_TABLE)
def test_reverse_list(n, result):
    """Test to verify function works."""
    from reverse_list import reverse_list
    assert reverse_list(n) == result
