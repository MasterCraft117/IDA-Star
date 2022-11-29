"""
Las funciones de creacion de archivos de input y output asi como el main estan implementadas en este archivo.
Para ejecutar, solo escribir "python3 main.py" en la consola.
"""

import sys
from state import State
from typing import Tuple, List
from idastar import ida_star

def take_input() -> State:
    with open('input.txt', 'r') as input_file:
        goal: List[Tuple[int, int, int]] = []
        for _ in range(3):
            goal.append(tuple(map(lambda x: int(x), input_file.readline().split())))

        input_file.readline()

        initial: List[Tuple[int, int, int]] = []
        for _ in range(3):
            initial.append(tuple(map(lambda x: int(x), input_file.readline().split()))
                           )
    return State(initial, goal)


#Main
if __name__ == '__main__':
    print('Ejecutando...')
    state: State = take_input() #El estado inicial se determina por las matrices objetivo e inicial

    sys.stdout = open('outputIDA.txt', 'w')
    res = ida_star(state) #Guarda el resultado de solucion en el archivo txt
    if res is None:
        print('Error') #En caso de no encontrar solucion imprime error
