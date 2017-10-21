"""Test for Kata: Beginner Series 1 School Paperwork."""


import pytest


PAPERWORK_TABLE = [([1, 3, 3]), ([4, 2, 8]),
                   ([0, 0, 0]), ([1, 3, 3])]


@pytest.mark.parametrize("n, m, result", PAPERWORK_TABLE)
def test_paperwork(n, m, result):
    """Test to verify function works."""
    from beginner_series_1_school_paperwork import paperwork
    assert paperwork(n, m) == result
