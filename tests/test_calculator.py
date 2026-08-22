import pytest

from calculator_improved import CalculatorEngine

@pytest.fixture
def calculator():
    return CalculatorEngine()


def test_addition(calculator):
    assert calculator.evaluate("10 + 5") == 15


def test_subtraction(calculator):
    assert calculator.evaluate("10 - 5") == 5


def test_multiplication(calculator):
    assert calculator.evaluate("10 * 5") == 50


def test_division(calculator):
    assert calculator.evaluate("10 / 5") == 2


def test_operator_symbols(calculator):
    assert calculator.evaluate("10 × 5") == 50
    assert calculator.evaluate("10 ÷ 5") == 2


def test_decimal_calculation(calculator):
    assert calculator.evaluate("2.5 * 4") == 10


def test_negative_numbers(calculator):
    assert calculator.evaluate("-10 + 5") == -5


def test_empty_expression(calculator):
    with pytest.raises(ValueError, match="Nothing to calculate"):
        calculator.evaluate("")


def test_invalid_expression(calculator):
    with pytest.raises(ValueError, match="Invalid expression"):
        calculator.evaluate("10 +")


def test_division_by_zero(calculator):
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        calculator.evaluate("10 / 0")


def test_unsupported_operator(calculator):
    with pytest.raises(ValueError, match="Unsupported operator"):
        calculator.evaluate("10 ** 2")