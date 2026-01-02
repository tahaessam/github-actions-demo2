# Calculator App

A simple and fast Python calculator application with basic mathematical operations.

## Features

- **Addition**: Add two numbers together
- **Subtraction**: Subtract one number from another
- **Multiplication**: Multiply two numbers
- **Division**: Divide one number by another (with zero-division protection)
- **Power**: Raise a number to a power
- **Modulo**: Get the remainder of division

## Installation

No external dependencies required! Just make sure you have Python 3.10 or higher installed.

```bash
python --version
```

## Usage

```python
from app import add, subtract, multiply, divide, power, modulo

# Addition
result = add(5, 3)  # Returns 8

# Subtraction
result = subtract(10, 4)  # Returns 6

# Multiplication
result = multiply(3, 4)  # Returns 12

# Division
result = divide(15, 3)  # Returns 5.0

# Power
result = power(2, 3)  # Returns 8

# Modulo
result = modulo(10, 3)  # Returns 1
```

## Running Tests

To run the test suite, first install pytest:

```bash
pip install pytest
```

Then run the tests:

```bash
pytest test_app.py
```

Or with verbose output:

```bash
pytest test_app.py -v
```

## CI/CD

This project uses GitHub Actions for continuous integration. Tests automatically run on:
- Every push to the `main` branch
- Every pull request to the `main` branch

## Error Handling

The `divide()` and `modulo()` functions include protection against division by zero:

```python
divide(10, 0)  # Raises ValueError: Cannot divide by zero
modulo(10, 0)  # Raises ValueError: Cannot divide by zero
```

## License

This project is open source and available for educational purposes.

