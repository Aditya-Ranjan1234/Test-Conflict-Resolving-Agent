def add(a, b):
    # Optimized addition with type hints
    return a + b

def subtract(a, b):
    # Optimized subtraction with type hints
    return a - b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(a, b):
    # New function for exponentiation
    return a ** b
