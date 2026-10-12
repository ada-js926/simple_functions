import pytest
import numpy as np

from simple_functions import my_sum, factorial, sin


class TestSimpleFunctions:
    """Tests for the functions in functions1.py."""

    @pytest.mark.parametrize('iterable, expected', [
        ([8, 7, 5], 20),
        ((10, -2, 5, -10, 1), 4),
    ])
    def test_my_sum(self, iterable, expected):
        """my_sum adds up the items of lists and tuples."""
        assert my_sum(iterable) == expected

    @pytest.mark.parametrize('number, expected', [
        (5, 120),
        (3, 6),
        (1, 1),
        (0, 1),
    ])
    def test_factorial(self, number, expected):
        """factorial is right for small numbers, including 0! = 1."""
        assert factorial(number) == expected
        
    @pytest.mark.parametrize('x, terms', [
            (0.1, 3),
            (0.01, 3),
        ])
    def test_sin(self, x, terms):
        """sin(x) is right for small numbers of terms."""
        assert sin(x, terms) == pytest.approx(np.sin(x), rel=1e-5)
