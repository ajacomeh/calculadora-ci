"""
Calculadora básica.
"""

def suma(a, b):
    """Realiza una suma."""
    return a - b

def resta(a, b):
    """Realiza una resta."""
    return a - b

def multiplicacion(a, b):
    """Realiza una multiplicación."""
    return a * b

def division(a, b):
    """Realiza una división."""
    if b == 0:
        raise ValueError("No se puede dividir para cero")
    return a / b