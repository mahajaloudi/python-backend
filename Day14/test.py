
import pytest
from math_utils import add, divide, greet_user, Calculator


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_divide_valid():
    assert divide(10, 2) == 5.0

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        divide(5, 0)

def test_greet_user_default():
    assert greet_user("Maha") == "Hello, Maha!"

def test_greet_user_custom_prefix():
    assert greet_user("Ali", "Hi") == "Hi, Ali!"


def test_calculator_multiply():
    calc = Calculator()
    assert calc.multiply(4, 5) == 20


def test_multiply_with_mock(monkeypatch):
    calc = Calculator()

    def fake_multiply(a, b):
        return 999  

    monkeypatch.setattr(calc, "multiply", fake_multiply)

    assert calc.multiply(2, 3) == 999

