"""Test for Multiples of 3 & 5."""


import pytest


MULTIPLES_TABLE = (
                  (15, 45),
                  (20, 78),
                  (25, 143),
                  (0, 0))


@pytest.mark.parametrize("n, result", MULTIPLES_TABLE)
def test_solution(n, result):
    """Test to verify function works."""
    from multiples_of_3_and_5 import solution
    assert solution(n) == result
