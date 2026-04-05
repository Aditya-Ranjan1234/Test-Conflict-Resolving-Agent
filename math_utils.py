def add(a, b):
    # Mathematical addition with precision
    return a + b

def subtract(a, b):
    # Mathematical subtraction with precision
    return a - b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def absolute(a):
    # New function for absolute value
    return abs(a)

def factorial(n):
    # New function for factorial
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
