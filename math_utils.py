def add(a, b):
    # Simplified addition without comments
    return a + b

def subtract(a, b):
    # Simplified subtraction without comments
    return a - b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def square_root(a):
    # New function for square root
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return a ** 0.5
