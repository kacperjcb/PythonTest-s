def gcd_iterative(a, b):
    if a < 0 or b < 0:
        raise ValueError("Argumenty powinny być liczbami nieujemnymi")

    while b:
        a, b = b, a % b
    return a


def gcd_recursive(a, b):
    if a < 0 or b < 0:
        raise ValueError("Argumenty powinny być liczbami nieujemnymi")

    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)
