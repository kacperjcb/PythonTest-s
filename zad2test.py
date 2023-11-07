import pytest
from zad2 import fibonacci_iterative, fibonacci_recursive  # Importuj moduł z implementacją funkcji



def test_fibonacci_iterative_positive():
    assert fibonacci_iterative(1) == 0
    assert fibonacci_iterative(2) == 1
    assert fibonacci_iterative(5) == 3
    assert fibonacci_iterative(10) == 34

def test_fibonacci_iterative_negative():
    with pytest.raises(ValueError):
        fibonacci_iterative(0)



def test_fibonacci_recursive_positive():
    assert fibonacci_recursive(1) == 0
    assert fibonacci_recursive(2) == 1
    assert fibonacci_recursive(5) == 3
    assert fibonacci_recursive(10) == 34

def test_fibonacci_recursive_negative():
    with pytest.raises(ValueError):
        fibonacci_recursive(-1)


if __name__ == "__main__":
    pytest.main()