def add(a, b):
    # Refactored addition with error handling
    try:
        return a + b
    except TypeError:
        raise ValueError("Invalid input types for addition")

def subtract(a, b):
    # Refactored subtraction with error handling
    try:
        return a - b
    except TypeError:
        raise ValueError("Invalid input types for subtraction")

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    try:
        return a / b
    except TypeError:
        raise ValueError("Invalid input types for division")

def modulo(a, b):
    # New function for modulo operation
    if b == 0:
        raise ValueError("Cannot perform modulo by zero")
    return a % b
