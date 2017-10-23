"""Kata 7kyu: Sum of the first nth term of Series."""


def series_sum(n):
	"""The Func returns a float as a string."""
    if n == 0:
        return "0.00"
    else:
        answer = sum([1 / (i * 3 - 2) for i in range(1, n+1)])
        return "%.2f" % answer
