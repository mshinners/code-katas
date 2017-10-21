"""Get Nth Even Number."""


def nth_even(n):
    """Testing to get all even numbers in a given list."""
    def is_even(n):
        return n % 2 == 0
    if n == 1:
        return False
    if n == 0 or n == 2:
        return True
    return enumerate(n)
#     for i in range(:):
