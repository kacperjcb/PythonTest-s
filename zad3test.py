import pytest
from zad3 import factorial_iterative, factorial_recursive



def test_factorial_iterative_positive():
    assert factorial_iterative(0) == 1
    assert factorial_iterative(1) == 1
    assert factorial_iterative(5) == 120
    assert factorial_iterative(10) == 3628800







def test_factorial_recursive_positive():
    assert factorial_recursive(0) == 1
    assert factorial_recursive(1) == 1
    assert factorial_recursive(5) == 120
    assert factorial_recursive(10) == 3628800




if __name__ == "__main__":
    pytest.main()
