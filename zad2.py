
def fibonacci_iterative(n):
    if n <= 0:
        raise ValueError("N musi być liczbą całkowitą dodatnią")
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib = [0, 1]
        for i in range(2, n):
            next_fib = fib[i - 1] + fib[i - 2]
            fib.append(next_fib)
        return fib[-1]

def fibonacci_recursive(n):
    if n < 0:
        raise ValueError("N musi być liczbą całkowitą nieujemną")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)