def add(a: float, b: float) -> float:
    """Fast addition operation."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Fast subtraction operation."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Fast multiplication operation."""
    return a * b


def divide(a: float, b: float) -> float:
    """Fast division operation."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a: float, b: float) -> float:
    """Fast exponentiation operation."""
    return a ** b


def modulo(a: float, b: float) -> float:
    """Fast modulo operation."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a % b
    