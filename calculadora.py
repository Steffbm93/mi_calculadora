# calculadora.py

def sumar(a: float, b: float) -> float:
    """Suma dos números y devuelve el resultado."""
    return a + b

def restar(a: float, b: float) -> float:
    """Resta el segundo número al primero y devuelve el resultado."""
    return a - b

def multiplicar(a: float, b: float) -> float:
    """Multiplica dos números y devuelve el resultado."""
    return a * b

def dividir(a: float, b: float) -> float:
    """Divide el primer número por el segundo.
    
    Lanza un error si se intenta dividir por cero.
    """
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b

def potencia(a: float, b: float) -> float:
    """Calcula a elevado a la b."""
    return a ** b

def cubo(a: float) -> float:
    """Calcula el cubo de un número (a elevado a la 3)."""
    return a ** 3


if __name__ == "__main__":
    print("Suma:", sumar(8, 12))             # 20
    print("Resta:", restar(15, 6))           # 9
    print("Multiplicación:", multiplicar(3, 7))  # 21
    print("División:", dividir(25, 5))       # 5.0
   


