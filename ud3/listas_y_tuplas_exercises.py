
"""Ejercicio 1
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemá�cas, Física,
Química, Historia y Lengua) en una lista y la muestre por pantalla."""

asignaturas = ["matematicas", "fisica", "quimica", "historia", "lengua"]
print(asignaturas)

"""Ejercicio 2
Escribir un programa que almacene las asignaturas de un curso (por ejemplo, Matemá�cas,
Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio
<asignatura>, donde <asignatura> es cada una de las asignaturas de la lista."""
asignaturas = ["matematicas", "fisica", "quimica", "historia", "lengua"]

for i in range(len(asignaturas)):
    print("Yo estudio " + asignaturas[i])

"""Ejercicio 3
Escribir un programa que almacene las asignaturas de un curso (por ejemplo, Matemá�cas,
Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en
cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado
<nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las
correspondientes notas introducidas por el usuario."""


asignaturas = ["matematicas", "fisica", "quimica", "historia", "lengua"]
notas = []

for i in range(len(asignaturas)):
    nota = float(input("Dime la asignatura de " + asignaturas[i]))
    notas.append(nota)

for i in range(len(asignaturas)):
    print("En " + asignaturas[i] + " has sacado un " + str(notas[i]))


"""Ejercicio 4
Escribir un programa que pregunte al usuario los números ganadores de la lotería primi�va, los
almacene en una lista y los muestre por pantalla ordenados de menor a mayor."""

numeros = []

for i in range(5):
    numero = int(input("Dime el numero ganador numero " + str(i + 1)))
    numeros.append(numero)
numeros.sort()
print(numeros)

"""Ejercicio 5
Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla
en orden inverso separados por comas."""

nums = []

for i in range(10):
    nums.append(i + 1)
nums.reverse()
print(nums)

"""Ejercicio 6
Escribir un programa que almacene las asignaturas de un curso (por ejemplo, Matemá�cas,
Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en
cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar
por pantalla las asignaturas que el usuario �ene que repe�r."""
asignaturas = ["matematicas", "fisica", "quimica", "historia", "lengua"]
suspendidas = []
for i in range(len(asignaturas)):
    nota = float(input("Dime la nota de " + asignaturas[i]))
    if nota < 5:
        suspendidas.append(asignaturas[i])
print(suspendidas)


"""Ejercicio 7
Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que
ocupen posiciones múl�plos de 3, y muestre por pantalla la lista resultante.
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u',
'v', 'w', 'x', 'y', 'z']"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u',
'v', 'w', 'x', 'y', 'z']
cuenta = 3
for i in range(len(alphabet), 1, -1):
    if i % 3 == 0:
        alphabet.pop(i -1)


print(alphabet)

"""Ejercicio 8
Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo."""

palabra = input("Escribe una palabra: ")

palabra = list(palabra)

palabra_inversa = palabra
palabra_inversa.reverse()

if palabra_inversa == palabra:
    print("Es palíndroma")
else:
    print("No es palíndroma")


"""Ejercicio 9
Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces
que con�ene cada vocal."""

palabra = input("Escribe una palabra: ")

a = palabra.count("a")
e = palabra.count("e")
i = palabra.count("i")
o = palabra.count("o")
u = palabra.count("u")

print("A = " + str(a))
print("E = " + str(e))
print("I = " + str(i))
print("O = " + str(o))
print("U = " + str(u))


"""Ejercicio 10
Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8,
y muestre por pantalla el menor y el mayor de los precios."""

precios = [50, 75, 46, 22, 80, 65, 8]

precios.sort()

print("El precio mas bajo es: " + str(precios[0]))
print("El precio mas alto es: " + str(precios[-1]))

"""Ejercicio 11
Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por
pantalla su producto escalar."""

vector1 = set([1, 2, 3])
vector2 = set([-1, 0, 2])

print(vector1 & vector2)

"""Ejercicio 12
Escribir un programa que almacene las matrices en una lista y muestre por pantalla su producto.
Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector
fila en una lista."""

a = ((1, 2, 3), (4, 5, 6))
b = ((-1, 0), (0, 1), (1,1))
result = [[0,0], [0,0]]
for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            result[i][j] += a[i][k] * b[k][j]
for i in range(len(result)):
    result[i] = tuple(result[i])
result = tuple(result)
for i in range(len(result)):
    print(result[i])





"""Ejercicio 13
Escribir un programa que pregunte por una muestra de números, separados por comas, los
guarde en una lista y muestre por pantalla su media y desviación �pica."""
