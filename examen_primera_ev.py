def operacion_suma_y_media():
    numeros = []
    print("Debes introducir 10 numeros: ")

    for i in range(10):
        valor = float(input(f"Introduce el numero en posición {i + 1}: "))
        numeros.append(valor)

    total_suma = sum(numeros)
    media = total_suma / len(numeros)

    return total_suma, media


def comprobar_numeros():
    num1 = float(input("Introduce el primer numero: "))
    num2 = float(input("Introduce el segundo numero: "))
    num3 = float(input("Introduce el tercer numero: "))

    if num1 == num2 == num3:
        print("Los tres numeros son iguales.")
    elif num1 != num2 and num1 != num3 and num2 != num3:
        print("Los tres numeros son distintos.")
    else:
        print("Hay dos numeros iguales.")
