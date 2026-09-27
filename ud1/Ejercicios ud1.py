


"""Ejercicio 1
Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!."""

print("¡Hola Mundo!")


"""Ejercicio 2
Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por
pantalla el contenido de la variable."""

cadena = "Hola Mundo!"
print(cadena)


"""Ejercicio 3
Escribir un programa que pregunte el nombre del usuario en la consola y después de que el
usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el
nombre que el usuario haya introducido."""

nombre = input("Ingrese su nombre: ")
print("Hola " + nombre)



"""Ejercicio 4
Escribir un programa que muestre por pantalla el resultado de la siguiente operación
aritmé�ca (
3+2
2⋅5 )2."""

resultado = (((3+2) / (2*5)) ** 2)


"""Ejercicio 5
Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por
hora. Después debe mostrar por pantalla la paga que le corresponde."""

horasTrabajadas = float(input("Cuantas horas has trabajado?"))
costePorHora = float(input("A que precio se cobra la hora"))

paga = horasTrabajadas * costePorHora

print(paga)



"""Ejercicio 6
Escribir un programa que lea un entero posi�vo, n, introducido por el usuario y después muestre
en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los n primeros enteros
posi�vos puede ser calculada de la siguiente forma:
suma = 𝑛𝑛(𝑛𝑛 + 1)
2"""

n = int(input("Ingrese un numero entero positivo: "))

suma = (n * (n + 1)) / 2

print("La suma de los primeros numeros enteros hasta " + str(suma) + " es " + str(n))



"""Ejercicio 7
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice
de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de
masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con
dos decimales."""

peso = float(input("Ingresa tu peso: "))
estatura = float(input("Ingresa tu estatura: "))

imc = round(float(peso)/float(estatura)**2,2)

print("Tu indice de masa corporal es " + str(imc))



"""Ejercicio 8
Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n>
entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por
el usuario, y <c> y <r> son el cociente y el resto de la división entera respec�vamente."""

num1 = int(input("Ingrese un primer numero entero: "))
num2 = int(input("Ingrese un segundo numero entero: "))

cociente = num1 / num2
resto = num1 % num2

print("El resultado de la división es: " + str(cociente) + " y el resto es: " + str(resto))


"""Ejercicio 9
Escribir un programa que pregunte al usuario una can�dad a inver�r, el interés anual y el número
de años, y muestre por pantalla el capital obtenido en la inversión."""

cantidad = float(input("Indica la cantidad de dinero a invertir: "))
interes = float(input("Indica el interes anual elegido: "))
años = int(input("Indica los años que quieres invertir: "))

interesReal = interes / 100

resultadoPrestamo = cantidad * interesReal * años

print("El capital total despues de " + str(años) + " años de inversión es de: " + str(resultadoPrestamo))



"""Ejercicio 10
Una juguetería �ene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta
por correo y la empresa de logís�ca les cobra por peso de cada paquete así que deben calcular
el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa
112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas
vendidos en el úl�mo pedido y calcule el peso total del paquete que será enviado."""

pesoPayaso = 112
pesoMuñeca = 75

totalPayasos = 15
totalMuñecas = 20

pesoTotalUltimoPedido = (totalPayasos * pesoPayaso) + (totalMuñecas * pesoMuñeca)

print("El precio total del paquete será: " + str(round(pesoTotalUltimoPedido, 2)))

"""Ejercicio 11
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año.
Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance
final de tu cuenta de ahorros. Escribir un programa que comience leyendo la can�dad de dinero
depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe
calcular y mostrar por pantalla la can�dad de ahorros tras el primer, segundo y tercer años.
Redondear cada can�dad a dos decimales."""

interes = 0.04

cantidadInicial = float(input("Indica la cantidad de dinero inicial: "))

cantidadPrimerAño = (cantidadInicial * interes) + cantidadInicial
cantidadSegundoAño = (cantidadPrimerAño * interes) + cantidadPrimerAño
cantidadTercerAño = (cantidadSegundoAño * interes) + cantidadSegundoAño

print("Cantidad primer año: " + str(round(cantidadPrimerAño, 2)))
print("Cantidad segundo año: " + str(round(cantidadSegundoAño, 2)))
print("Cantidad tercer año: " + str(round(cantidadTercerAño, 2)))



"""Ejercicio 12
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día �ene un descuento
del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son
del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento
que se le hace por no ser fresca y el coste final total."""

precioBarra = 3.49
precioBarraAyer = precioBarra - (precioBarra * 0.6)

print("El precio habitual de una barra es de: "
      + str(precioBarra) + " pero si la barra es de ayer se le aplica un "
                           "descuento del 60% por lo cual su precio pasa a ser "
                           "de: " + str(round(precioBarraAyer, 2)))




