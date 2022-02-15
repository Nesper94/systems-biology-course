#!/usr/bin/env python3
# Tomado del libro "Automate the boring stuff with Python: Practical
# programming for total beginners" de Al Sweigart

import random, time, copy
WIDTH = 60
HEIGHT = 20

# Crear una lista de listas para las celdas:
nextCells = []
celdaViva = '#' # Definir el caracter usado para representar una celda viva

for x in range(WIDTH):
    column = [] # Crear una nueva columna.
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append(celdaViva) # Añadir una celda viva.
        else:
            column.append(' ') # Añadir una celda muerta

    nextCells.append(column) # nextCells es una lista de columnas.

while True: # Loop principal del programa.
    print('\n\n\n\n\n') # Separar cada paso con nuevas líneas.
    currentCells = copy.deepcopy(nextCells)

    # Imprimir currentCells en la pantalla:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='') # Imprimir el # o el espacio.
        print() # Imprimir una nueva línea al final de la fila.

    # Calcular el próximo paso basado en las celdas existentes (currentCells):
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Obtener coordenadas de los vecinos:
            # `% WIDTH` se asegura que leftCoord esté siempre entre 0 y WIDTH - 1
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            # Contar el número de vecinos vivos:
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == celdaViva:
                numNeighbors += 1 # Si el vecino de arriba a la izquierda está vivo.
            if currentCells[x][aboveCoord] == celdaViva:
                numNeighbors += 1 # Si el vecino de arriba está vivo.
            if currentCells[rightCoord][aboveCoord] == celdaViva:
                numNeighbors += 1 # Si el vecino de arriba a la derecha está vivo.
            if currentCells[leftCoord][y] == celdaViva:
                numNeighbors += 1 # Si el vecino de la izquierda está vivo.
            if currentCells[rightCoord][y] == celdaViva:
                numNeighbors += 1 # Si el vecino de la derecha está vivo.
            if currentCells[leftCoord][belowCoord] == celdaViva:
                numNeighbors += 1 # Si el vecino de abajo a la izquierda está vivo.
            if currentCells[x][belowCoord] == celdaViva:
                numNeighbors += 1 # Si el vecino de abajo está vivo.
            if currentCells[rightCoord][belowCoord] == celdaViva:
                numNeighbors += 1 # Si el vecino de abajo a la derecha está vivo.

            # Actualizar el estado de cada celda basado en las reglas del juego Vida de Conway:
            if currentCells[x][y] == celdaViva and (numNeighbors == 2 or numNeighbors == 3):
                # Celdas vivas con 2 o 3 vecinos siguen estando vivas:
                nextCells[x][y] = celdaViva
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                # Celdas muertas con 3 vecinos se vuelven celdas vivas:
                nextCells[x][y] = celdaViva
            else:
                # Todo lo demás muere o se queda muerto:
                nextCells[x][y] = ' '

    time.sleep(1) # Añadir una pausa de 1 segundo para reducir el parpadeo.
