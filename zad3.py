def factorial_iterative(n):
    if n < 0:
        raise ValueError("Argument n musi być liczbą nieujemną")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    if n < 0:
        raise ValueError("Argument n musi być liczbą nieujemną")
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)
