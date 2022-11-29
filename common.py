"""
Funciones auxiliares comunes utilizadas en el algoritmo
"""

import numpy as np

def print_helper(arr: np.array): #Funcion auxiliar que imprimir las matrices de estado
    pr_str = ''
    for i in range(9):
        pr_str += str(arr[i]) + ' '
        if (i + 1) % 3 == 0:
            pr_str += '\n'
    print(pr_str)
