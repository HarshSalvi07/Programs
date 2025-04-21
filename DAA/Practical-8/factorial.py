def factorial(n):
    if n < 0:
        return False
    if n <= 1:
        return n
    return n * factorial(n-1)
