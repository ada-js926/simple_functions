__all__ = ['my_sum', 'factorial']


def my_sum(iterable):
    """Return the sum of the items in iterable."""
    tot = 0
    for i in iterable:
        tot += i
    return tot


def factorial(n):
    """Return n! (n factorial) for a non-negative integer n."""
    return n * factorial(n-1) if n else 1

def sin(x, terms=1):
    """Approximate sin(x) by summing the first terms of its Taylor series."""
    return sum((-1)**k * x**(2*k+1) / factorial(2*k+1) for k in range(terms))