"""
Simple Calculator Module
===================
This module provides basic mathematical operations including addition, subtraction,
multiplication, division, and more advanced operations like power and modulo.

All functions are designed to work with numeric types (int, float).
"""


def add(a: float, b: float) -> float:
    """
    Add two numbers together.
    
    This function takes two numeric values and returns their sum.
    It can handle both integers and floating-point numbers.
    
    Args:
        a (float): The first number to add
        b (float): The second number to add
    
    Returns:
        float: The sum of a and b
    
    Examples:
        >>> add(5, 3)
        8
        >>> add(2.5, 3.7)
        6.2
        >>> add(-10, 5)
        -5
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """
    Subtract the second number from the first number.
    
    This function performs subtraction: a - b.
    It can handle both integers and floating-point numbers.
    
    Args:
        a (float): The number to subtract from (minuend)
        b (float): The number to subtract (subtrahend)
    
    Returns:
        float: The result of a - b
    
    Examples:
        >>> subtract(10, 4)
        6
        >>> subtract(5.5, 2.3)
        3.2
        >>> subtract(3, 7)
        -4
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers together.
    
    This function takes two numeric values and returns their product.
    It can handle both integers and floating-point numbers.
    
    Args:
        a (float): The first number to multiply
        b (float): The second number to multiply
    
    Returns:
        float: The product of a and b
    
    Examples:
        >>> multiply(4, 5)
        20
        >>> multiply(2.5, 4)
        10.0
        >>> multiply(-3, 7)
        -21
    """
    return a * b


def divide(a: float, b: float) -> float:
    """
    Divide the first number by the second number.
    
    This function performs division: a / b.
    Note: Division by zero will raise a ZeroDivisionError.
    
    Args:
        a (float): The dividend (number to be divided)
        b (float): The divisor (number to divide by)
    
    Returns:
        float: The result of a / b
    
    Raises:
        ZeroDivisionError: If b is zero
    
    Examples:
        >>> divide(10, 2)
        5.0
        >>> divide(15, 3)
        5.0
        >>> divide(7, 2)
        3.5
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return a / b


def power(base: float, exponent: float) -> float:
    """
    Raise a number to a power.
    
    This function calculates base raised to the power of exponent.
    It uses the ** operator for exponentiation.
    
    Args:
        base (float): The base number
        exponent (float): The exponent (power to raise base to)
    
    Returns:
        float: The result of base raised to the power of exponent
    
    Examples:
        >>> power(2, 3)
        8.0
        >>> power(5, 2)
        25.0
        >>> power(2, 0.5)
        1.4142135623730951  # Square root of 2
    """
    return base ** exponent


def modulo(a: float, b: float) -> float:
    """
    Calculate the remainder after division.
    
    This function returns the remainder when a is divided by b.
    Also known as the modulus operation.
    
    Args:
        a (float): The dividend
        b (float): The divisor
    
    Returns:
        float: The remainder of a divided by b
    
    Raises:
        ZeroDivisionError: If b is zero
    
    Examples:
        >>> modulo(10, 3)
        1.0
        >>> modulo(15, 4)
        3.0
        >>> modulo(20, 5)
        0.0
    """
    if b == 0:
        raise ZeroDivisionError("Cannot perform modulo operation with zero divisor!")
    return a % b


def absolute(value: float) -> float:
    """
    Get the absolute value of a number.
    
    This function returns the absolute value (non-negative value) of a number.
    If the number is negative, it returns its positive equivalent.
    
    Args:
        value (float): The number to get the absolute value of
    
    Returns:
        float: The absolute value of the input number
    
    Examples:
        >>> absolute(-5)
        5.0
        >>> absolute(5)
        5.0
        >>> absolute(-3.7)
        3.7
    """
    return abs(value)


def maximum(a: float, b: float) -> float:
    """
    Return the larger of two numbers.
    
    This function compares two numbers and returns the greater value.
    
    Args:
        a (float): The first number to compare
        b (float): The second number to compare
    
    Returns:
        float: The larger of the two numbers
    
    Examples:
        >>> maximum(5, 10)
        10.0
        >>> maximum(-3, -7)
        -3.0
        >>> maximum(3.5, 3.5)
        3.5
    """
    return max(a, b)


def minimum(a: float, b: float) -> float:
    """
    Return the smaller of two numbers.
    
    This function compares two numbers and returns the lesser value.
    
    Args:
        a (float): The first number to compare
        b (float): The second number to compare
    
    Returns:
        float: The smaller of the two numbers
    
    Examples:
        >>> minimum(5, 10)
        5.0
        >>> minimum(-3, -7)
        -7.0
        >>> minimum(3.5, 3.5)
        3.5
    """
    return min(a, b)
    