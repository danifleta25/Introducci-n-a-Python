
import re
texto = "El precio es 10.99 y el código es ABC123 y el email es danifleta25@gmail.com."
"""Ejercicio 1
Encontrar un número decimal."""
patron_decimal = r"\d+\.\d+"
decimal = re.findall(patron_decimal, texto)
print(decimal)

""""Ejercicio 2.
Encontrar todas las palabras de 3 letras minúsculas"""
patron_minus = r"[a-z]{3}"
minus = re.findall(patron_minus, texto)
print(minus)

"""Ejercicio 3.
Validar si la cadena comienza con "El precio"""""
patron_inicio = r"^El precio"
inicio = re.match(patron_inicio, texto)
if inicio:
    print("La cadena compienza con \"El precio\"")

"""Ejercicio 4.
Encontrar el código (patrón que incluye letras y números)"""
patron_letras_numeros = r"[A-Z]{3}\d{3}"
letras_num = re.findall(patron_letras_numeros, texto)
print(letras_num)

import re
texto_email = "Contacto: usuario1@ejemplo.com o usuario2@subdominio.otro.es"

"""Ejercicio 5.
Extraer todas las direcciones de correo electrónico usando `findall` y 
separando usuario de dominio"""
patron_email = r"([a-zA-Z0-9_.+-]+)@([a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)$"
email = re.findall(patron_email, texto_email)
for e in email:
    print(f"Nombre de usuario: {e[0]}, Dominio: {e[1]}")

"""Ejercicio 6.
Reemplazar el dominio genérico "ejemplo.com"""""
patron_reemplazar = r"ejemplo\.com"
reemplazar = re.sub(patron_reemplazar, "gmail.com", texto_email)
print(reemplazar)
"""Ejercicio 7.
Buscar un patrón sensible a mayúsculas y minúsculas con `IGNORECASE`"""
texto_case = "Python es potente. No solo python."

patron_python = r"python"
resultado = re.findall(patron_python, texto_case, re.IGNORECASE)
print(resultado)