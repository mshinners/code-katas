"""Test Replace all Items module."""


import pytest


ITEM_REPLACEMENT_TABLE = (
    ([9, 8, 3], 3, 7, [9, 8, 7]),
    ([7, 7, 8], 8, 7, [7, 7, 7]),
    ("Learning code is fun!", 'f', 's', "Learning code is sun!"),
    ("I like mike n ikes", 'i', 'o', "I loke moke n okes"))


@pytest.mark.parametrize("n, m, o, result", ITEM_REPLACEMENT_TABLE)
def test_replace_all(n, m, o, result):
    """Test to verify function works."""
    from replace_all_items import replace_all
    assert replace_all(n, m, o) == result


# tests = (
#     (([], 1, 2), []),
#     (([1, 2, 2], 1, 2), [2, 2, 2]),
#     (([1, 1, 2], 1, 2), [2, 2, 2]),
#     (([1, 2, 1, 2, 3], 1, 2), [2, 2, 2, 2, 3]),
#     (("Hello World", 'o', '0'), "Hell0 W0rld"),
# )

# for t in tests:
#     inp, exp = t
#     test.assert_equals(replace_all(*inp), exp)
