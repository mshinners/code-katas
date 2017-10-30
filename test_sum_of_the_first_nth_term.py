"""TEST for: Kata 7kyu: Sum of the first nth term of Series."""


import pytest


# Commented out so as not to disrupt pytest
# Test.assert_equals(series_sum(1), "1.00")
# Test.assert_equals(series_sum(2), "1.25")
# Test.assert_equals(series_sum(3), "1.39")


def test_series_sum():
    """Test that function finds the right number."""
    from sum_of_the_first import series_sum
    assert series_sum(1) == "1.00"


def test_series_sum_2():
    """Test that function finds the right number."""
    from sum_of_the_first import series_sum
    assert series_sum(24) == "2.10"


def test_series_sum_3():
    """Test that function finds the right number."""
    from sum_of_the_first import series_sum
    assert series_sum(42) == "2.29"
