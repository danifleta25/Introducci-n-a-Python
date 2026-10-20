

"""Ejercicio 1
Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'},
pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no
está en el diccionario."""
from fileinput import close

divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
user_option = input("Introduce la moneda: ")
if user_option.capitalize() in divisas:
    print(divisas[user_option.capitalize()])
else:
    print("Esa moneda no esta en la lista")

"""Ejercicio 2
Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde
en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años,
vive en <dirección> y su número de teléfono es <teléfono>."""
name = input("Dime tu nombre: ")
age = int(input("Dime tu edad: "))
adress = input("Dime tu direccion: ")
tlf = int(input("Dime tu telefono: "))

datos = {"nombre":name, "edad": age, "direccion":adress, "telefono":tlf}

print(datos["nombre"] + " tiene " + str(datos["edad"]) + " años, vive en " + str(datos["direccion"]) + " y su numero de telefono es " + str(datos["telefono"]))


"""Ejercicio 3
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte
al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de
kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
Fruta Precio
Plátano 1.35
Manzana 0.80
Fruta Precio
Pera 0.85
Naranja 0.70"""

frutas = {"Platano":1.35, "Manzana":0.80, "Pera":0.85, "Naranja":0.70}

userOption = input("Que fruta quieres?")
kilos = int(input("Cuantos kilos quieres?"))

if userOption.capitalize() in frutas:
    precio = frutas[userOption.capitalize()] * kilos
    print("Precio total: ", precio)
else:
    print("Esa fruta no esta en la lista")

"""Ejercicio 4
Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla
la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.
meses = {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio', 7:'julio',
8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'}"""

meses = {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio', 7:'julio',
8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'}

fecha = input("Introduce una fecha en formato dd/mm/aaaa: ")

lista = list(fecha.split("/"))
mes = int(lista[1])

if mes in meses:
    print(lista[0], " de ", meses[mes], " de ", lista[2])
else:
    print("Error")


"""Ejercicio 6
Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una
persona (por ejemplo, nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al
usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario."""

datos = {}
continuar = True

while continuar:
    categoria = input("Que categoria de dato quieres introducir sobre ti?")
    dato = input("Introduce el dato correspondiente a la categoria: ")
    datos.update({categoria:dato})
    print(datos)

    respuesta = input("Quieres añadir mas datos? (S/N)")
    if respuesta == "N":
        continuar = False



"""Ejercicio 7
Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa
debe preguntar el ar�culo y su precio y añadir el par al diccionario, hasta que el usuario decida
terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el
siguiente formato
Lista de la compra
Ar�culo 1 Precio
Ar�culo 2 Precio
Ar�culo 3 Precio"""

cesta = {}
continuar = True

while continuar:
    articulo = input("Nombre articulo: ")
    precio = float(input("Precio: "))
    cesta.update({articulo:precio})
    respuesta = input("Seguir comprando?(S/N)")
    if respuesta == "N":
        continuar = False

print("LISTA DE LA COMPRA")
for clave, valor in cesta.items():
    print(clave, " - ", valor, "€")

"""Ejercicio 8
Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá
las palabras en español e inglés separadas por dos puntos, y cada
par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las
palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para
traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir."""

diccionario = {}
palabras = input("Introduce una palabra y su traducción separadas por una coma: ")
parejas = palabras.lower().split(",")

for pareja in parejas:
        separadas = pareja.split(":")
        diccionario.update({separadas[0].strip():separadas[1].strip()})

frase = input("Introduce una frase en español para traducir: ")
frase = frase.split()
traduccion = ""
for palabra in frase:
        if palabra.lower() in diccionario:
            traduccion += diccionario[palabra.lower()] + " "
        else:
            traduccion += palabra + " "

print(traduccion)


"""Ejercicio 9
Escribir un programa que ges�one las facturas pendientes de cobro de una empresa. Las facturas
se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el
valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva
factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el
número de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se
preguntará por el número de factura y se eliminará del diccionario. Después de cada operación
el programa debe mostrar por pantalla la can�dad cobrada hasta el momento y la can�dad
pendiente de cobro."""

facturas = {}

terminar = True
print("BIENVENIDO AL PROGRAMA DE FACTURACIÓN")
while terminar:
    print("1) Añadir factura\n2) Pagar factura\n3)Terminar")
    option = int(input("Seleccione un número"))
    if option == 1:
        num_factura = int(input("Introduce el numero de la factura a añadir: "))
        coste = float(input("Introduce el coste de la factura: "))
        facturas.update({num_factura:coste})
        print("FACTURA AÑADIDA")
    if option == 2:
        num_factura = int(input("Introduce el numero de la factura a pagar: "))
        facturas.pop(num_factura)
        print("FACTURA ELIMINADA")
    if option == 3:
        print("CERRANDO EL PROGRAMA...")
        terminar = False





"""Ejercicio 10
Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los
clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, y el valor
será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente),
donde preferente tendrá el valor True si se trata de un cliente preferente. El programa debe
preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente,
(3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. En
función de la opción elegida el programa tendrá que hacer lo siguiente:
1. Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de
datos.
2. Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
3. Preguntar por el NIF del cliente y mostrar sus datos.
4. Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
5. Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
6. Terminar el programa."""

clientes = {}

#MENU
option = ""
print("GESTIÓN CLIENTES")
while option != 6:
    print("(1) Añadir cliente\n(2) Eliminar cliente\n(3) Mostrar cliente\n(4) Listar todos los clientes"
          "\n(5) Listar clientes preferentes\n(6) Terminar")
    option = int(input("Elige un número: "))

    if option == 1:
        nif = input("Introduce el NIF del cliente: ")
        nombre = input("Introduce el nombre del cliente: ")
        direccion = input("Introduce la direccion del cliente: ")
        tlf = input("Introduce el telefono del cliente: ")
        email = input("Introduce el email del cliente: ")
        preferente = input("Preferente?(True/False)")
        if preferente.lower() == "true":
            preferente = True
        if preferente.lower() == "false":
            preferente = False
        else:
            print("Debes introducir \"True\" o \"False\"")

        cliente = {
            "Nombre":nombre,
            "Direccion":direccion,
            "Telefono":tlf,
            "Correo":email,
            "Preferente":preferente
        }
        clientes[nif] = cliente
        print("Añadiendo cliente...")
    if option == 2:
        nif = input("Introduce el NIF del cliente a eliminar de la base de datos: ")
        if nif in clientes:
            clientes.pop(nif)
            print("Cliente eliminado")
        else:
            print("El cliente no esta en la BD")
    if option == 3:
        nif = input("Introduce el NIF del cliente a mostrar: ")
        if nif in clientes:
            cliente = clientes[nif]
            print(cliente)
        else:
            print("El cliente no esta en la BD")
    if option == 4:
        print("Mostrando lista completa de clientes: ")
        for clave, valor in clientes.items():
            print(clave, " - ", valor["Nombre"])
    if option == 5:
        for clave, valor in clientes.items():
            if valor["Preferente"] == True:
                print(clave, " - ", valor["Nombre"])
    if option == 6:
        print("Cerrando el programa")
        break




"""Ejercicio 11
El directorio de los clientes de una empresa está organizado en una cadena de texto como la de
más abajo, donde cada línea con�ene la información del nombre, email, teléfono, nif, y el
descuento que se le aplica. Las líneas se separan con el carácter de cambio de línea \n y la
primera línea con�ene los nombres de los campos con la información contenida en el directorio.
"nif;nombre;email;teléfono;descuento\n01234567L;Luis
González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena
Ramírez;macarena@mail.com;692839321;8\n63823376M;JuanJosé
Mar�nez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen
Sánchez;carmen@mail.com;667677855;15.7"
Escribir un programa que genere un diccionario con la información del directorio, donde cada
elemento corresponda a un cliente y tenga por clave su nif y por valor otro diccionario con el
resto de la información del cliente. Los diccionarios con la información de cada cliente tendrán
como claves los nombres de los campos y como valores la información de cada cliente
correspondientes a los campos. Es decir, un diccionario como el siguiente:"""
"""{'01234567L': {'nombre': 'Luis González', 'email': 'luisgonzalez@mail.com', 'teléfono':
'656343576', 'descuento': 12.5}, '71476342J': {'nombre': 'Macarena Ramírez', 'email':
'macarena@mail.com', 'teléfono': '692839321', 'descuento': 8.0}, '63823376M':
{'nombre': 'Juan José Mar�nez', 'email': 'juanjo@mail.com', 'teléfono': '664888233',
'descuento': 5.2}, '98376547F': {'nombre': 'Carmen Sánchez', 'email':
'carmen@mail.com', 'teléfono': '667677855', 'descuento': 15.7}}"""
