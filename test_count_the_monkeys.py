"""Test Count the Monkeys module."""


import pytest


MONKEY_COUNT_TABLE = [[2, [1, 2]],
                      [4, [1, 2, 3, 4]],
                      [3, [1, 2, 3]],
                      [5, [1, 2, 3, 4, 5]]]


@pytest.mark.parametrize("n, result", MONKEY_COUNT_TABLE)
def test_monkey_count(n, result):
    """Test to verify function works."""
    from count_the_monkeys import monkey_count
    assert monkey_count(n) == result
