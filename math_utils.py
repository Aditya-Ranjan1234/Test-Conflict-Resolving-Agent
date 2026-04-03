def add(a, b):
    # This is a simple addition
    return a + b

def subtract(a, b):
    # This is a simple subtraction
    return a - b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
