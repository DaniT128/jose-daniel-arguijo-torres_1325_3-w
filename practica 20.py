def factorial(n):
    if n <= 1:  # Condición de finalización
        return 1
    else:
        return n * factorial(n - 1)  # Llamada recursiva

# Ejemplo de uso
print(factorial(5))  # Devuelve 120, ya que 5! = 5 * 4 * 3 * 2 * 1
