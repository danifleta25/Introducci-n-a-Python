
"""Ejercicio 1
Escribir una función que muestre por pantalla el saludo ¡Hola amiga! cada vez que se la invoque"""
import math
from shlex import split


def saludo_amiga():
    print("¡Hola amiga!")
    return
saludo_amiga()

"""Ejercicio 2
Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el
saludo ¡hola <nombre>!."""

def saludo(nombre):
    print("¡Hola " + nombre + "!")
    return
saludo("Dani")


"""Ejercicio 3
Escribir una función que reciba un número entero posi�vo y devuelva su factorial."""

def factorial(numero):
    total= 1

    for i in range(numero):
        total *= i + 1
    return total
print(factorial(6))

"""Ejercicio 4
Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe
recibir la can�dad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se
invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%."""

def calculo_iva(cantidad, iva = 21):
    return cantidad + (cantidad * (iva / 100))

print(str(calculo_iva(1000)) + "€")



"""Ejercicio 5
Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro
usando la primera función."""
def area_circulo(radio):
    return math.pi * (radio ** 2)

def volumen_cilindro(altura, radio):
    radio = area_circulo(radio)
    return altura * radio

print(volumen_cilindro(3, 2))



"""Ejercicio 6
Escribir una función que reciba una muestra de números en una lista y devuelva su media."""

numeros = [2, 3, 5, 7]

def media(lista_numeros):
    return sum(lista_numeros) / len(lista_numeros)

print(media(numeros))

"""Ejercicio 7
Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con
sus cuadrados."""
numeros = [2, 3, 5, 7]

def cuadrado(lista_numeros):
    lista = []
    for i in lista_numeros:
        lista.append(i ** 2)
    return lista

print(cuadrado(numeros))


"""Ejercicio 8
Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario
con su media, varianza y desviación �pica"""
numeros = [2, 3, 5, 7]

def statistics(listanum):
    dicci = {}

    dicci["media"] = sum(listanum) / len(listanum)
    dicci["varianza"] = sum(cuadrado(listanum))/ len(listanum) - dicci["media"]**2
    dicci["tipica"] = dicci["varianza"] ** 0.5

    return dicci

print(statistics(numeros))



"""Ejercicio 9
Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el
mínimo común múl�plo"""




"""Ejercicio 10
Escribir una función que convierta un número decimal en binario y otra que convierta un número
binario en decimal."""

"""Ejercicio 11
Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada
palabra que con�ene y su frecuencia. Escribir otra función que reciba el diccionario generado
con la función anterior y devuelva una tupla con la palabra más repe�da y su frecuencia."""

def contador_palabras(frase):
    dic = {}
    frase = frase.split()
    for palabra in frase:
        if palabra in dic:
            dic[palabra] += 1
        else:
            dic[palabra] = 1
    return dic

def top_palabra(frase):
    palabra_max = ""
    frecuencia_palabra = 0
    for word, freq in frase.items():
        if freq > frecuencia_palabra:
            frecuencia_palabra = freq
            palabra_max = word
    return palabra_max, frecuencia_palabra

texto = 'Como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera'

print(contador_palabras(texto))

print(top_palabra(contador_palabras(texto)))





