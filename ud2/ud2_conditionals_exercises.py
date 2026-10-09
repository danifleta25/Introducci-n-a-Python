"""Ejercicio 1
Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad
o no."""
from fileinput import close
from ssl import create_default_context

age = int(input("Ingrese su edad: "))

if age >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

"""Ejercicio 2
Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el
usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas."""

password = "creed"

userPass = input("Ingrese su contraseña: ")

if userPass.upper() == password.upper():
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")

"""Ejercicio 3
Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el
divisor es cero el programa debe mostrar un error."""

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))

if num2 == 0:
    print("No se puede dividir por 0")
else:
    print(num1 / num2)

"""Ejercicio 4
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o
impar."""

numDiv = int(input("Introduce un numero entero: "))

if numDiv % 2 == 0:
    print("Tu numero es par")
else:
    print("Tu numero es impar")

"""Ejercicio 5
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos
iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad
y sus ingresos mensuales y muestre por pantalla si el usuario �ene que tributar o no."""

age = int(input("Introduce tu edad: "))
ingresos = float(input("Introduce tus ingresos mensuales"))

if age >= 16 and ingresos >= 1000:
    print("Tienes que tributar.")
else:
    print("No tienes que tributar.")

"""Ejercicio 6
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El
grupo A está formado por las mujeres con un nombre anterior a la M y los hombres con un
nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario
su nombre y sexo, y muestre por pantalla el grupo que le corresponde."""

name = input("Introduce tu nombre:")
sexo = input("Introduce tu sexo (Hombre/Mujer): ")

inicial = name.index("0")

if sexo == "Hombre" and name.lower()[0] > "n":
    print("Perteneces al grupo A")
elif sexo == "Mujer" and name.lower()[0] < "m":
    print("Perteneces al grupo A")
else:
    print("Perteneces al grupo B")

"""Ejercicio 7
Los tramos imposi�vos para la declaración de la renta en un determinado país son los siguientes:
Renta Tipo imposi�vo
Menos de 10000€ 5%
Entre 10000€ y 20000€ 15%
Entre 20000€ y 35000€ 20%
Entre 35000€ y 60000€ 30%
Más de 60000€ 45%
Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el �po
imposi�vo que le corresponde."""

rentaAnual = float(input("Introduce tu renta anual: "))

if rentaAnual < 10000:
    print("Te corresponde un 5%")
elif rentaAnual >= 10000 and rentaAnual < 20000:
    print("Te corresponde un 15%")
elif rentaAnual >= 20000 and rentaAnual < 35000:
    print("Te corresponde un 20%")
elif rentaAnual >= 35000 and rentaAnual < 60000:
    print("Te corresponde un 30%")
else:
    print("Te corresponde un 45%")

"""Ejercicio 8
En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que
pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en
mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o
más, pero no valores intermedios entre las cifras mencionadas. A con�nuación, se muestra una
tabla con los niveles correspondientes a cada puntuación. La can�dad de dinero conseguida en
cada nivel es de 2.400€ mul�plicada por la puntuación del nivel.
Nivel Puntuación
Inaceptable 0.0
Aceptable 0.4
Meritorio 0.6 o más
Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así
como la can�dad de dinero que recibirá el usuario."""

puntuacion = input("Indica tu nivel de rendimiento(Inaceptable/Aceptable/Meritorio: ")

if puntuacion.lower() == "inaceptable":
    print("La cantidad de dinero recibida es: 0")
elif puntuacion.lower() == "Aceptable":
    print("La cantidad de dinero recibida es: " + str(2400 * 0.4))
elif puntuacion.lower() == "Meritorio":
    print("La cantidad de dinero recibida es: " + str(2400 * 0.6))
else:
    print("No has introducido un nivel de rendimiento válido")

"""Ejercicio 9
Escribir un programa para una empresa que �ene salas de juegos para todas las edades y quiere
calcular de forma automá�ca el precio que debe cobrar a sus clientes por entrar. El programa
debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es
menor de 4 años puede entrar gra�s, si �ene entre 4 y 18 años debe pagar 5€ y si es mayor de
18 años, 10€."""

age = int(input("Ingrese su edad: "))

if age <= 4:
    print("La entrada es gratis")
elif 4 < age < 18:
    print("La entrada son 5€")
else:
    print("La entrada son 10€")

"""Ejercicio 10
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los
ingredientes para cada �po de pizza aparecen a con�nuación.
• Ingredientes vegetarianos: Pimiento y tofu.
• Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función
de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se
puede elegir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al
final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes
que lleva."""

print("___BIENVENIDO A LA PIZZERIA BELLA NAPOLI___")
print()
dieta = input("Eres vegetariano o NO vegetariano?")

if dieta.lower() == "vegetariano":
    print("Ingredientes: Pimiento y tofu.")
elif dieta.lower() == "no vegetariano":
    print("Ingredientes: Peperoni, Jamon y Salmon")
    close();
else:
    print("Introduce correctamente ""Vegetariano"" o ""No vegetariano""")
    close();