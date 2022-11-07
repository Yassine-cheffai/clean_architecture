import pytest

from .main import SimpleCalculator


def test_add_two_numbers():
    calculator = SimpleCalculator()
    result = calculator.add(4, 5)
    assert result == 9


def test_add_three_numbers():
    calculator = SimpleCalculator()
    result = calculator.add(4, 5, 6)
    assert result == 15


def test_add_many_numbers():
    numbers = range(100)
    calculator = SimpleCalculator()
    result = calculator.add(*numbers)
    assert result == 4950


def test_sub_two_numbers():
    calculator = SimpleCalculator()
    result = calculator.sub(10, 7)
    assert result == 3


def test_mul_two_numbers():
    calculator = SimpleCalculator()
    result = calculator.mul(6, 4)
    assert result == 24


def test_mul_many_numbers():
    calculator = SimpleCalculator()
    numbers = range(1, 10)
    result = calculator.mul(*numbers)
    assert result == 362880

def test_div_two_numbers_float():
    calculator = SimpleCalculator()
    result = calculator.div(13, 2)
    assert result == 6.5

def test_div_by_zero_return_inf():
    calculator = SimpleCalculator()
    result = calculator.div(5, 0)
    assert result == float("inf")

def test_mul_by_zero_raises_exception():
    calculator = SimpleCalculator()
    with pytest.raises(ValueError):
        calculator.mul(3, 0)

def test_avg_simple():
    calculator = SimpleCalculator()
    assert calculator.avg([2, 5, 12, 98]) == 29.25

def test_avg_with_upper_threshold():
    calculator = SimpleCalculator()
    assert calculator.avg([2, 5, 12, 98], ut=90) == calculator.avg([2, 5, 12])

def test_avg_with_lower_threshold():
    calculator = SimpleCalculator()
    assert calculator.avg([2, 5, 12, 98], lt=10) == calculator.avg([12, 98])

def test_avg_with_lower_and_upper_threshold():
    calculator = SimpleCalculator()
    assert calculator.avg([2, 5, 12, 98], lt=10, ut=90) == calculator.avg([12])

def test_avg_with_empty_list():
    calculator = SimpleCalculator()
    assert calculator.avg([]) == 0

def test_avg_with_empty_list_after_limiting():
    calculator = SimpleCalculator()
    assert calculator.avg([12, 98], lt=15, ut=90) == 0

def test_avg_with_empty_list_and_ut_lt():
    calculator = SimpleCalculator()
    assert calculator.avg([], lt=15, ut=90) == 0