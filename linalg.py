#!/usr/bin/env python3
# Juan Camilo Arboleda Rivera 2022

import numpy as np
import matplotlib.pyplot as plt

origen = np.array([0,0])

# Definimos la matriz
m = np.array([[1.5, 0.5],
              [0.5, 1.5]])

# Definimos la exponenciación de matrices
# Aunque numpy ya tiene implementada la función
# numpy.linalg.matrix_power(a, n), esta es una buena oportunidad para
# recordar cómo definir funciones recursivas
def expm(matrix, exp):
    if exp == 0:
        return np.array([[1,0],
                         [0,1]])
    else:
        return matrix.dot(expm(matrix, exp-1))

# Creamos las gráficas
n_plots = 4
fig, axs = plt.subplots(1, n_plots, figsize=(16,8))

for ax in axs:
    ax.set(ylim=(-6,6), xlim=(-6,6))
    ax.set_aspect(1)

n_vec = 16 # Potencia de 2 mayor o igual a 8 para tener el vector {1,1}

for exp in range(n_plots):
    for i in range(n_vec): # Creamos cada vector y lo multiplicamos por la matriz
        vec = np.array([np.cos(2*np.pi*i/n_vec), np.sin(2*np.pi*i/n_vec)])
        vec = expm(m, exp).dot(vec)
        axs[exp].quiver(*origen, *vec, angles='xy', scale_units='xy', scale=1)

plt.show()
