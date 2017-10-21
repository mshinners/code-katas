"""Kata: Beginner Series 1 School Paperwork.

AliSkinner, CrazyMerlyn, acaccia, NaMe613, SquishyStrawberry, Grzegorz Wild (plus 100 more warriors)

def paperwork(n, m):
    return n * m if n > 0 and m > 0 else 0
"""


def paperwork(n, m):
    """Calculate how mmuch paper is needed."""
    if n <= 0 or m <= 0:
        return 0
    return n * m
