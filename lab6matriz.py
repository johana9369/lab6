import os
import readchar
import random
import time
from typing import List, Tuple
from readchar import readkey, key


with open('map1.txt', 'r') as map1:
   map1 = map1.read()
    # Haz algo con el contenido del archivo
print(map1)
time.sleep(3)

with open('map2.txt', 'r') as map2:
    map2 = map2.read()
    # Haz algo con el contenido del archivo
print(map2)
time.sleep(3)

def convertir_laberinto_a_matriz(map1):
    # Dividir las líneas del laberinto
    lineas = map1.strip().split('\n')
    
    # Utilizar map para convertir cada línea en una lista de caracteres
    matriz = list(map(list, lineas))
    
    return matriz

# Ejemplo de uso:
map1_str = """
#########
#S      #
#   #####
#   #   #
#####   #
#     E #
#########
"""

matriz_laberinto = convertir_laberinto_a_matriz(map1_str)

# Imprimir la matriz resultante
for fila in matriz_laberinto:
    print(fila)

def convertir_laberinto_a_matriz(map2):
    # Dividir las líneas del laberinto
    lineas = map2.strip().split('\n')
    
    # Utilizar map para convertir cada línea en una lista de caracteres
    matriz = list(map(list, lineas))
    
    return matriz

# Ejemplo de uso:
map2_str = """
#########
#S      #
#   #####
#   #   #
#####   #
#     E #
#########
"""

matriz_laberinto = convertir_laberinto_a_matriz(map2_str)

# Imprimir la matriz resultante
for fila in matriz_laberinto:
    print(fila)    