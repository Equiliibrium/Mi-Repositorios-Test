


OPERACIONES = {
    "1": ("Suma", lambda a, b: a + b),
    "2": ("Resta", lambda a, b: a - b),
    "3": ("Multiplicación", lambda a, b: a * b),
    "4": ("División", lambda a, b: a / b),
}


def pedir_numero(mensaje):
    """Solicita un número decimal al usuario hasta que el valor sea válido."""
    while True:
        entrada = input(mensaje)
        try:
            return float(entrada)
        except ValueError:
            print("Entrada inválida. Debes escribir un número.")


def calcular():
    print("== Calculadora básica ==")

    while True:
        print("\nSelecciona una operación:")
        for clave, (nombre, _) in OPERACIONES.items():
            print(f"{clave}: {nombre}")

        opcion = input("Elige una opción (1-4) o escribe 'q' para salir: ").strip().lower()

        if opcion == "q":
            print("¡Hasta luego!")
            break

        if opcion not in OPERACIONES:
            print("Opción no válida, inténtalo nuevamente.")
            continue

        num1 = pedir_numero("Ingresa el primer número: ")
        num2 = pedir_numero("Ingresa el segundo número: ")

        nombre_operacion, funcion = OPERACIONES[opcion]

        if opcion == "4" and num2 == 0:
            print("No se puede dividir entre cero.")
            continue

        resultado = funcion(num1, num2)
        print(f"Resultado de {nombre_operacion.lower()}: {resultado}")


if __name__ == "__main__":
    calcular()


