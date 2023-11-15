import pytest
from zad1 import add, subtract, multiply, divide  # Importuj moduł z implementacją funkcji



def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-2, -3) == -5

def test_add_mixed_numbers():
    assert add(2, -3) == -1


def test_subtract_positive_numbers():
    assert subtract(5, 3) == 2

def test_subtract_negative_numbers():
    assert subtract(-5, -3) == -2

def test_subtract_mixed_numbers():
    assert subtract(5, -3) == 8



def test_multiply_positive_numbers():
    assert multiply(2, 3) == 6

def test_multiply_negative_numbers():
    assert multiply(-2, -3) == 6

def test_multiply_mixed_numbers():
    assert multiply(2, -3) == -6


def test_divide_positive_numbers():
    assert divide(6, 3) == 2

def test_divide_negative_numbers():
    assert divide(-6, -3) == 2

def test_divide_mixed_numbers():
    assert divide(6, -3) == -2

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(6, 0)



# Funkcja testująca dodawanie
def test_add_negative():
    assert add(2, 3) != 6  # Oczekiwane jest, że 2 + 3 nie równa się 6

# Funkcja testująca odejmowanie
def test_subtract_negative():
    assert subtract(5, 2) != 2  # Oczekiwane jest, że 5 - 2 nie równa się 2

# Funkcja testująca mnożenie
def test_multiply_negative():
    assert multiply(3, 4) != 14  # Oczekiwane jest, że 3 * 4 nie równa się 14

# Funkcja testująca dzielenie
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)  # Oczekiwane jest zgłoszenie błędu ValueError przy dzieleniu przez zero


if __name__ == "__main__":
    pytest.main()
