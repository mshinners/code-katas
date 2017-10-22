"""Kata 6 Multiples of 3 & 5.

Process, zyxwhut, lowicz, simpajj, benjaminfigueiredo, nueks
(plus 79 more warriors)

def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)
"""


def solution(number):
    """Here we find multiples of 3 & 5 out in the wild."""
    result = []
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            result.append(i)
    return sum(result)
