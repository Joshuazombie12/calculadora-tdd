import pytest
from src.calculator import Calculator
import math

calc = Calculator()

def test_add():
    assert calc.add(2.5, 1.5) == pytest.approx(4.0, rel=1e-9)

def test_sub():
    assert calc.sub(5.0, 3.2) == pytest.approx(1.8, rel=1e-9)

def test_mul():
    assert calc.mul(3.0, 2.5) == pytest.approx(7.5, rel=1e-9)

def test_div():
    assert calc.div(7.5, 2.5) == pytest.approx(3.0, rel=1e-9)
    with pytest.raises(ZeroDivisionError):
        calc.div(1, 0)

def test_sqrt_positive():
    for val in [0.0, 1.0, 2.0, 10.0, 123.456]:
        expected = math.sqrt(val)
        got = calc.sqrt(val, tol=1e-8)
        assert got == pytest.approx(expected, abs=1e-3)

def test_sqrt_negative():
    with pytest.raises(ValueError):
        calc.sqrt(-4.0)

def test_exp_small_positive():
    assert calc.exp(1.0) == pytest.approx(math.e, abs=1e-3)
    assert calc.exp(2.0) == pytest.approx(math.exp(2.0), abs=1e-3)

def test_exp_negative():
    assert calc.exp(-1.0) == pytest.approx(math.exp(-1.0), abs=1e-3)
