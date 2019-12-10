# -*- coding: utf-8 -*-

import re  # se importa la libreria de expresion regular

path = "archivoe.txt"  # llamando al primer archivo

# buscar el archivo para su uso dentro de programa
try:
    archivo = open(path, 'r')
except:
    print("El archivo no se encuentra")
    quit()

texto = ""

# busca las cadenas de caractere por linea
for linea in archivo:
    texto += linea


# Sentencia de asignación.
# Ejemplo: suma = 0, factorial = 1, vidas = cont, etc.
patronASIGNACION = r'([a-z0-9]+\s*[=]+\s*[a-z0-9+]+)'
resultadoASIGNACION = re.findall(patronASIGNACION, texto)
print("Las sentencias de asignacion son: ", resultadoASIGNACION)
print("")


# Operaciones aritméticas básicas.
# Ejemplo: suma = 2.7 + 3, cont = cont + 1, etc.
# ([a-z0-9-_]+\s*[=]+\s*[a-z0-9-_]+\s*[+,-,*,/,%]+\s*[a-z0-9-_]+)

#patronARITMETICO = r'([A-Za-z0-9-_]+\s*[=]+\s*[A-Za-z0-9-_|0-9.0-9]+\s*[\+,\-,\*,\/,\%]+\s*[A-Za-z0-9-_|0-9.0-9]+)'

patronARITMETICO = r'([a-z0-9]+\s*[=]\s*[a-z0-9|\d.\d]+\s*[\+\-\*\/]\s*[a-z0-9|\d.\d]+)'