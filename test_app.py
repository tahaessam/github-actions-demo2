"""
Unit Tests for Calculator Module
=================================
This module contains comprehensive unit tests for all mathematical functions
in the app.py calculator module.

Tests cover:
- Basic functionality
- Edge cases (negative numbers, zero, floating point)
- Error handling (division by zero, etc.)
"""

import pytest
from app import (
    add,
    subtract,
    multiply,
    divide,
    power,
    modulo,
    absolute,
    maximum,
    minimum
)


# ============================================================================
# ADDITION TESTS
# ============================================================================

def test_add_positive_integers():
    """Test addition with positive integers."""
    assert add(2, 3) == 5
    assert add(10, 20) == 30
    assert add(0, 5) == 5


def test_add_negative_numbers():
    """Test addition with negative numbers."""
    assert add(-5, -3) == -8
    assert add(-10, 5) == -5
    assert add(10, -5) == 5


def test_add_floating_point():
    """Test addition with floating point numbers."""
    assert add(2.5, 3.7) == 6.2
    assert add(0.1, 0.2) == pytest.approx(0.3)
    assert add(1.5, 2.5) == 4.0


def test_add_zero():
    """Test addition with zero."""
    assert add(0, 0) == 0
    assert add(5, 0) == 5
    assert add(0, 5) == 5


# ============================================================================
# SUBTRACTION TESTS
# ============================================================================

def test_subtract_positive_integers():
    """Test subtraction with positive integers."""
    assert subtract(10, 4) == 6
    assert subtract(20, 10) == 10
    assert subtract(5, 5) == 0


def test_subtract_negative_result():
    """Test subtraction that results in negative numbers."""
    assert subtract(3, 7) == -4
    assert subtract(5, 10) == -5


def test_subtract_negative_numbers():
    """Test subtraction with negative numbers."""
    assert subtract(-5, -3) == -2
    assert subtract(-10, 5) == -15
    assert subtract(10, -5) == 15


def test_subtract_floating_point():
    """Test subtraction with floating point numbers."""
    assert subtract(5.5, 2.3) == pytest.approx(3.2)
    assert subtract(10.0, 3.5) == 6.5


def test_subtract_zero():
    """Test subtraction with zero."""
    assert subtract(5, 0) == 5
    assert subtract(0, 5) == -5
    assert subtract(0, 0) == 0


# ============================================================================
# MULTIPLICATION TESTS
# ============================================================================

def test_multiply_positive_integers():
    """Test multiplication with positive integers."""
    assert multiply(3, 4) == 12
    assert multiply(5, 6) == 30
    assert multiply(10, 10) == 100


def test_multiply_negative_numbers():
    """Test multiplication with negative numbers."""
    assert multiply(-3, 7) == -21
    assert multiply(3, -7) == -21
    assert multiply(-3, -7) == 21


def test_multiply_floating_point():
    """Test multiplication with floating point numbers."""
    assert multiply(2.5, 4) == 10.0
    assert multiply(1.5, 2.5) == 3.75
    assert multiply(0.5, 0.5) == 0.25


def test_multiply_zero():
    """Test multiplication with zero."""
    assert multiply(5, 0) == 0
    assert multiply(0, 5) == 0
    assert multiply(0, 0) == 0


def test_multiply_one():
    """Test multiplication with one (identity element)."""
    assert multiply(5, 1) == 5
    assert multiply(1, 5) == 5


# ============================================================================
# DIVISION TESTS
# ============================================================================

def test_divide_positive_integers():
    """Test division with positive integers."""
    assert divide(10, 2) == 5.0
    assert divide(9, 3) == 3.0
    assert divide(15, 5) == 3.0


def test_divide_floating_point():
    """Test division with floating point numbers."""
    assert divide(7, 2) == 3.5
    assert divide(10.5, 2.5) == 4.2
    assert divide(1, 3) == pytest.approx(0.3333333333333333)


def test_divide_negative_numbers():
    """Test division with negative numbers."""
    assert divide(-10, 2) == -5.0
    assert divide(10, -2) == -5.0
    assert divide(-10, -2) == 5.0


def test_divide_by_one():
    """Test division by one."""
    assert divide(5, 1) == 5.0
    assert divide(10.5, 1) == 10.5


def test_divide_zero_dividend():
    """Test division of zero by a number."""
    assert divide(0, 5) == 0.0
    assert divide(0, -5) == 0.0


def test_divide_by_zero_error():
    """Test that division by zero raises ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError) as exc_info:
        divide(10, 0)
    assert "Cannot divide by zero!" in str(exc_info.value)


# ============================================================================
# POWER TESTS
# ============================================================================

def test_power_positive_integers():
    """Test power operation with positive integers."""
    assert power(2, 3) == 8.0
    assert power(5, 2) == 25.0
    assert power(3, 4) == 81.0


def test_power_zero_exponent():
    """Test power operation with zero exponent."""
    assert power(5, 0) == 1.0
    assert power(10, 0) == 1.0
    assert power(-5, 0) == 1.0


def test_power_one_exponent():
    """Test power operation with exponent of one."""
    assert power(5, 1) == 5.0
    assert power(10, 1) == 10.0


def test_power_fractional_exponent():
    """Test power operation with fractional exponent (square root)."""
    assert power(4, 0.5) == pytest.approx(2.0)
    assert power(9, 0.5) == pytest.approx(3.0)
    assert power(2, 0.5) == pytest.approx(1.4142135623730951)


def test_power_negative_base():
    """Test power operation with negative base."""
    assert power(-2, 3) == -8.0
    assert power(-3, 2) == 9.0


# ============================================================================
# MODULO TESTS
# ============================================================================

def test_modulo_positive_integers():
    """Test modulo operation with positive integers."""
    assert modulo(10, 3) == 1.0
    assert modulo(15, 4) == 3.0
    assert modulo(20, 5) == 0.0


def test_modulo_floating_point():
    """Test modulo operation with floating point numbers."""
    assert modulo(10.5, 3) == pytest.approx(1.5)
    assert modulo(15.7, 4.2) == pytest.approx(3.1)


def test_modulo_negative_numbers():
    """Test modulo operation with negative numbers."""
    assert modulo(-10, 3) == 2.0
    assert modulo(10, -3) == -2.0


def test_modulo_zero_dividend():
    """Test modulo operation with zero dividend."""
    assert modulo(0, 5) == 0.0
    assert modulo(0, 10) == 0.0


def test_modulo_by_zero_error():
    """Test that modulo by zero raises ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError) as exc_info:
        modulo(10, 0)
    assert "Cannot perform modulo operation with zero divisor!" in str(exc_info.value)


# ============================================================================
# ABSOLUTE VALUE TESTS
# ============================================================================

def test_absolute_positive_numbers():
    """Test absolute value with positive numbers."""
    assert absolute(5) == 5.0
    assert absolute(10.5) == 10.5
    assert absolute(0) == 0.0


def test_absolute_negative_numbers():
    """Test absolute value with negative numbers."""
    assert absolute(-5) == 5.0
    assert absolute(-10.5) == 10.5
    assert absolute(-3.7) == 3.7


def test_absolute_zero():
    """Test absolute value of zero."""
    assert absolute(0) == 0.0
    assert absolute(-0) == 0.0


# ============================================================================
# MAXIMUM TESTS
# ============================================================================

def test_maximum_positive_integers():
    """Test maximum function with positive integers."""
    assert maximum(5, 10) == 10.0
    assert maximum(10, 5) == 10.0
    assert maximum(7, 7) == 7.0


def test_maximum_negative_numbers():
    """Test maximum function with negative numbers."""
    assert maximum(-3, -7) == -3.0
    assert maximum(-10, -5) == -5.0


def test_maximum_mixed_signs():
    """Test maximum function with mixed positive and negative numbers."""
    assert maximum(-5, 5) == 5.0
    assert maximum(5, -5) == 5.0


def test_maximum_floating_point():
    """Test maximum function with floating point numbers."""
    assert maximum(3.5, 3.5) == 3.5
    assert maximum(2.3, 5.7) == 5.7
    assert maximum(10.1, 10.0) == 10.1


def test_maximum_with_zero():
    """Test maximum function with zero."""
    assert maximum(0, 5) == 5.0
    assert maximum(-5, 0) == 0.0
    assert maximum(0, 0) == 0.0


# ============================================================================
# MINIMUM TESTS
# ============================================================================

def test_minimum_positive_integers():
    """Test minimum function with positive integers."""
    assert minimum(5, 10) == 5.0
    assert minimum(10, 5) == 5.0
    assert minimum(7, 7) == 7.0


def test_minimum_negative_numbers():
    """Test minimum function with negative numbers."""
    assert minimum(-3, -7) == -7.0
    assert minimum(-10, -5) == -10.0


def test_minimum_mixed_signs():
    """Test minimum function with mixed positive and negative numbers."""
    assert minimum(-5, 5) == -5.0
    assert minimum(5, -5) == -5.0


def test_minimum_floating_point():
    """Test minimum function with floating point numbers."""
    assert minimum(3.5, 3.5) == 3.5
    assert minimum(2.3, 5.7) == 2.3
    assert minimum(10.1, 10.0) == 10.0


def test_minimum_with_zero():
    """Test minimum function with zero."""
    assert minimum(0, 5) == 0.0
    assert minimum(-5, 0) == -5.0
    assert minimum(0, 0) == 0.0