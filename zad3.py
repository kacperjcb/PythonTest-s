def factorial_iterative(n):
    if n < 0:
        return -1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    if n < 0:
        return -1
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)