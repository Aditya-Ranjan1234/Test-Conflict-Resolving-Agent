# Math Utils

A lightweight Python library providing common arithmetic utility functions with input validation.

## Functions

| Function | Description |
|---|---|
| `add(a, b)` | Returns the sum of `a` and `b` |
| `subtract(a, b)` | Returns the difference `a - b` |
| `multiply(a, b)` | Returns the product of `a` and `b` |
| `divide(a, b)` | Returns the quotient `a / b` (raises `ValueError` if `b` is zero) |
| `power(a, b)` | Returns `a` raised to the power of `b` |

`add` and `subtract` validate that both inputs are numeric (`int` or `float`) and raise a `TypeError` otherwise.

## Requirements

- Python 3.x
- [pytest](https://pytest.org/) (for running tests)

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

```python
import math_utils

math_utils.add(3, 4)        # 7
math_utils.subtract(10, 3)  # 7
math_utils.multiply(3, 4)   # 12
math_utils.divide(10, 2)    # 5.0
math_utils.power(2, 8)      # 256
```

## Running Tests

```bash
pytest
```
