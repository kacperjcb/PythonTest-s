def gcd_iterative(a, b):
    while b:
        a, b = b, a % b
    return a



def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)
