from calculadora import (
    suma,
    resta,
    multiplicacion,
    division
)

def test_suma():
    assert suma(5, 3) == 8

def test_resta():
    assert resta(10, 4) == 6

def test_multiplicacion():
    assert multiplicacion(2, 3) == 6

def test_division():
    assert division(10, 2) == 5