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