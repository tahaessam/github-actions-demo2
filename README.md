# Calculator App

A comprehensive Python calculator application with basic and advanced mathematical operations. This project includes a well-documented calculator module with unit tests and CI/CD integration.

## Features

### Basic Operations
- **Addition**: Add two numbers together
- **Subtraction**: Subtract one number from another
- **Multiplication**: Multiply two numbers
- **Division**: Divide one number by another (with zero-division protection)

### Advanced Operations
- **Power**: Raise a number to a power
- **Modulo**: Get the remainder of division
- **Absolute Value**: Get the absolute value of a number
- **Maximum**: Return the larger of two numbers
- **Minimum**: Return the smaller of two numbers

### Code Quality
- ✅ Comprehensive unit tests (43+ test cases)
- ✅ Type hints for all functions
- ✅ Detailed docstrings with examples
- ✅ Error handling for edge cases
- ✅ CI/CD with GitHub Actions

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd demo-vid
```

2. Install dependencies (for running tests):
```bash
pip install -r requirements.txt
```

3. Verify Python version (Python 3.10 or higher required):
```bash
python --version
```

## Usage

### Basic Operations

```python
from app import add, subtract, multiply, divide

# Addition
result = add(5, 3)  # Returns 8.0
result = add(2.5, 3.7)  # Returns 6.2

# Subtraction
result = subtract(10, 4)  # Returns 6.0
result = subtract(5.5, 2.3)  # Returns 3.2

# Multiplication
result = multiply(3, 4)  # Returns 12.0
result = multiply(2.5, 4)  # Returns 10.0

# Division
result = divide(15, 3)  # Returns 5.0
result = divide(7, 2)  # Returns 3.5
```

### Advanced Operations

```python
from app import power, modulo, absolute, maximum, minimum

# Power (exponentiation)
result = power(2, 3)  # Returns 8.0
result = power(4, 0.5)  # Returns 2.0 (square root)

# Modulo (remainder)
result = modulo(10, 3)  # Returns 1.0
result = modulo(15, 4)  # Returns 3.0

# Absolute Value
result = absolute(-5)  # Returns 5.0
result = absolute(-3.7)  # Returns 3.7

# Maximum
result = maximum(5, 10)  # Returns 10.0
result = maximum(-3, -7)  # Returns -3.0

# Minimum
result = minimum(5, 10)  # Returns 5.0
result = minimum(-3, -7)  # Returns -7.0
```

### Import All Functions

```python
from app import (
    add, subtract, multiply, divide,
    power, modulo, absolute,
    maximum, minimum
)
```

## Running Tests

The project includes comprehensive unit tests covering all functions with 43+ test cases including edge cases and error handling.

### Install Test Dependencies

```bash
pip install -r requirements.txt
```

### Run Tests

Run all tests:
```bash
pytest test_app.py
```

Run with verbose output:
```bash
pytest test_app.py -v
```

Run with coverage report:
```bash
pytest test_app.py --cov=app --cov-report=html
```

### Test Coverage

The test suite covers:
- ✅ All 9 mathematical functions
- ✅ Positive and negative numbers
- ✅ Integer and floating-point operations
- ✅ Edge cases (zero, negative numbers)
- ✅ Error handling (division by zero, etc.)
- ✅ Mixed number types

## CI/CD

This project uses GitHub Actions for continuous integration. Tests automatically run on:
- Every push to the `main` branch
- Every pull request to the `main` branch

## Error Handling

The `divide()` and `modulo()` functions include protection against division by zero:

```python
try:
    result = divide(10, 0)  # Raises ZeroDivisionError
except ZeroDivisionError as e:
    print(e)  # "Cannot divide by zero!"

try:
    result = modulo(10, 0)  # Raises ZeroDivisionError
except ZeroDivisionError as e:
    print(e)  # "Cannot perform modulo operation with zero divisor!"
```

## Project Structure

```
demo-vid/
├── app.py              # Main calculator module with all functions
├── test_app.py         # Comprehensive unit tests
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── .github/
    └── workflows/
        └── ci.yml      # GitHub Actions CI/CD configuration
```

## Development

### Code Quality Features

- **Type Hints**: All functions include type annotations
- **Docstrings**: Comprehensive documentation with examples
- **Error Handling**: Proper exception handling for edge cases
- **Testing**: Full test coverage with pytest

### Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add/update tests
5. Ensure all tests pass
6. Submit a pull request

## License

This project is open source and available for educational purposes.

