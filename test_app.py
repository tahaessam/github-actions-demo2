from app import add, multiply, divide, power, modulo


def test_add():
    assert add(2, 3) == 5


def test_multiply():
    assert multiply(3, 4) == 12


def test_divide():
    assert divide(10, 2) == 5.0
    assert divide(9, 3) == 3.0


def test_power():
    assert power(2, 3) == 8
    assert power(5, 2) == 25


def test_modulo():
    assert modulo(10, 3) == 1
    assert modulo(15, 5) == 0