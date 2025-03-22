# Calculadora de Factorial
# Autor: Nicolas Garcia - Samuel Arciniegas
# Licencia: MIT - Este código es libre y puede ser modificado y distribuido.

def calcular_factorial(numero):
    """
    Calcula el factorial de un número positivo.
    
    Args:
        numero (int): El número del cual calcular el factorial
        
    Returns:
        int: El factorial del número
    """
    if numero < 0:
        return "Error: El factorial solo está definido para números positivos"
    elif numero == 0 or numero == 1:
        return 1   
    else:
        factorial = 1
        for i in range(2, numero + 1):
            factorial *= i
        return factorial

if __name__ == "__main__":
    try:
        num = int(input("Ingrese un número positivo para calcular su factorial: "))
        resultado = calcular_factorial(num)
        print(f"El factorial de {num} es: {resultado}")
    except ValueError:
        print("Error: Por favor ingrese un número entero válido")
