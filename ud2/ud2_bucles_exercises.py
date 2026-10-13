


"""Ejercicio 1
Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces."""
from fileinput import close

palabra = input("Introduce una palabra: ")
contador = 0
"""Opcion1"""
while contador < 10:
    print(palabra)
    contador += 1

"""Opcion2"""
for i in range(10):
    print(palabra)

"""Ejercicio 2
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que
ha cumplido (desde 1 hasta su edad)."""
age = int(input("Introduce tu edad: "))
contador = 1

while contador <= age:
    print (contador)
    contador += 1




"""Ejercicio 3
Escribir un programa que pida al usuario un número entero posi�vo y muestre por pantalla todos
los números impares desde 1 hasta ese número separados por comas."""
num = int(input("Introduce un número entero positivo: "))

for i in range(num):
    if i % 2 == 1:
        print(i)





"""Ejercicio 4
Escribir un programa que pida al usuario un número entero posi�vo y muestre por pantalla la
cuenta atrás desde ese número hasta cero separados por comas."""
"Opcion 1"
numPos = int(input("Introduce un número entero positivo: "))

while numPos >= 0:
    print(numPos, end= ", ")
    numPos -= 1

"Opcion 2"
numPos = int(input("Introduce un número entero positivo: "))

for i in range(numPos, -1, -1):
    print(i, end=", ")

"""Ejercicio 5
Escribir un programa que pregunte al usuario una can�dad a inver�r, el interés anual y el número
de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión."""
cantidad = float(input("Ingresa la cantidad a invertir: "))
interes = float(input("Ingresa el interés acordado: "))
años = int(input("Introduce el número de años que quieres invertir el dinero: "))
contador = 1

while contador <= años:
    cantidadInteres = cantidad * (interes / 100) * contador
    print("Durante el año número " + str(contador) + " has obtenido un interés de: " + str(cantidadInteres))
    cantidad += cantidadInteres
    print("Y el saldo total ese año es de " + str(round(cantidad, 2)))
    contador += 1



"""Ejercicio 6
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo
rectángulo como el de más abajo, de altura el número introducido.
*
**
***
****
*****"""

num = int(input("Introduce un número entero: "))
star = "*"


for i in range(num):
    print(star)
    star += "*"




"""Ejercicio 7
Escribir un programa que muestre por pantalla la tabla de mul�plicar del 1 al 10."""
numMult = int(input("Introduce un numero del 1 al 9: "))

for i in range(10):
    print(str(numMult) + " * " + str(i + 1) + " = " + str(numMult * (i + 1)))




"""Ejercicio 8
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo
rectángulo como el de más abajo.
1
3 1
5 3 1
7 5 3 1
9 7 5 3 1"""

numEntero = int(input("Introduce un numero entero: "))

for i in range(1, numEntero + 1, 2):
    for j in range(i, 0, -2):
        print(j, end="")
    print()






"""Ejercicio 9
Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta."""

password = "pepa"
userPass = input("Introduce la contraseña: ")

while userPass != password:
    print("Contraseña incorrecta")
    userPass = input("Prueba de nuevo: ")

print("Contraseña correcta")


"""Ejercicio 10
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un
número primo o no."""
userNum = int(input("Introduce un numero entero mayor que 2: "))

for i in range(2, userNum):
    if userNum % i == 0:
        break

    if i + 1 == userNum:
        print("El numero es primo")
    else:
        print("El numero no es primo")




"""Ejercicio 11
Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las
letras de la palabra introducida empezando por la úl�ma."""
palabra = input("Introduce una palabra: ")
longitud = len(palabra)

while longitud > 0:
    print(palabra[longitud - 1], end="")
    longitud -= 1


"""Ejercicio 12
Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por
pantalla el número de veces que aparece la letra en la frase."""

frase = input("Introduce una frase: ")
letra = input("Introduce una letra que esté en la frase: ")

longitud = len(frase)
contador = 0

for i in range(longitud):
    if frase[i] == letra:
        contador += 1

print("La letra " + letra + " aparece un total de " + str(contador) + " veces.")



"""Ejercicio 13
Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el
usuario escriba “salir” que terminará."""

print("Si quieres cerrar el programa debes escribir \"salir\"")
userInput = ""

while userInput != "salir":
    userInput = input()
    if userInput == "salir":
        break
