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


def test_gcd_iterative_negative():
    with pytest.raises(ValueError):
        gcd_iterative(-1, 5)


def test_gcd_iterative_negative_2():
    with pytest.raises(ValueError):
        gcd_iterative(10, -5)


def test_gcd_recursive_negative():
    with pytest.raises(ValueError):
        gcd_recursive(-3, 7)


def test_gcd_recursive_negative_2():
    with pytest.raises(ValueError):
        gcd_recursive(8, -4)


if __name__ == "__main__":
    pytest.main()
