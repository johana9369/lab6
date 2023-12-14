import os
import readchar
import random
import time
from typing import List, Tuple
from readchar import readkey, key  

class Juego:
    def __init__(self, map1, map2):
        self.valor = map1
        self.mapa =  map2
        self.px = 0
        self.py = 0
        self.filas = "#"
        
    def valor_inicial(self, nombre):
        return self.valor
        #escriba su nombre
    nombre = input('escribe tu nombre: ')
    print(f'bienvenido a tu juego {nombre:}')
    print('\n Use las flechas para desplazarse')
    time.sleep(2)
      #crear los muros del laberionto

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


    def muros_laberintos(self, filas, pared_laberinto, end):
     #filas  para crear las paredes del laberinto
     filas = pared_laberinto.strip().split('\n')    
    #separo las filas con \n
     while len(filas) < end + 1:
        filas.append("#" * (end + 1 - len(filas)))
    #numero de filas incrementando en n+1
     for i in range(len(filas)):
        while len(filas[i]) < end + 1:
            filas[i] += '#'
    #suma de las partes del laberinto
     laberinto_partes = '\n'.join(filas)
     return laberinto_partes
   
    #matriz inicial
    def matriz(self, filas, pared_laberinto):
    #crear con la funcion flas la pared de laberinto
        filas = pared_laberinto.strip().split('\n')
        laberinto = [list(fila) for fila in filas]
        return laberinto
    
    def mostrar_laberinto_limpiar(laberinto):
     os.system('cls' if os.name == 'nt' else 'clear')  
     for fila in laberinto:
        print(''.join(fila))

    def main_loop(self, map1, map2, inicio, fin):
    # Desempaquetar las coordenadas de inicio
        self.px = 0
        self.py = 0
        px = 0
        py = 0
    # Bucle principal: continúa hasta que las coordenadas actuales sean iguales a las coordenadas de destino
        while (px, py) != fin:
    # Colocar el objeto en la posición actual en el mapa
            map1[py][px] = '☻'
    # Mostrar el laberinto actualizado en la consola
    def mostrar_laberinto_limpiar(self, map1, teclado):
        if teclado == key.UP and py > 0 and map1[py - 1][px] != '#':
           nueva_py -= 1
        elif teclado == key.DOWN and py < len(map1) - 1 and map1[py + 1][px] != '#':
           nueva_py += 1
        elif teclado == key.LEFT and px > 0 and map1[py][px - 1] != '#':
            nueva_px -= 1
        elif teclado == key.RIGHT and px < len(map1[0]) - 1 and map1[py][px + 1] != '#':
            nueva_px += 1

        # Limpiar la posición anterior del objeto en el mapa
        map1[py][px] = ' '

        # Actualizar las coordenadas actuales con las nuevas
        px, py = nueva_px, nueva_py
        if __name__ == "__proyec_6__":
            end = 20
    
    print(f" {nombre} finalizo el laberinto")