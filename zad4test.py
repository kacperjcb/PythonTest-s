import pytest
from zad4 import gcd_iterative, gcd_recursive


def test_gcd_iterative_positive():
    assert gcd_iterative(48, 18) == 6
    assert gcd_iterative(60, 48) == 12
    assert gcd_iterative(17, 8) == 1


def test_gcd_recursive_positive():
    assert gcd_recursive(48, 18) == 6
    assert gcd_recursive(60, 48) == 12
    assert gcd_recursive(17, 8) == 1

def test_gcd_iterative_failure():
    assert gcd_iterative(48, 18) == 42

if __name__ == "__main__":
    pytest.main()