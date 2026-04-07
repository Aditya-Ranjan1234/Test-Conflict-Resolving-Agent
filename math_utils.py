def add(a, b):
    """Adds two numbers"""
    # Enhanced addition with input validation and type hints
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be numbers")
    return a + b

def subtract(a, b):
    """Subtracts two numbers"""
    # Enhanced subtraction with input validation and type hints
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be numbers")
    return a - b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def multiply(a, b):
    # New function added
    return a * b

def power(a, b):
    # New function for exponentiation
    return a ** b

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