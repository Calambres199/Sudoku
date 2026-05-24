import pytest

from sudoku_pkg.sudoku import (
    print_grid,
    es_valido,
    solve_sudoku,
    there_is_another_solution
)

import pytest
from sudoku_pkg.sudoku import (
    es_valido,
    solve_sudoku,
    there_is_another_solution
)

def test_es_valido():
    sudoku = [
        [5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]
    ]
    assert es_valido(sudoku) == True

def test_solve_sudoku():
    sudoku = [
        [5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]
    ]
    assert solve_sudoku(sudoku) == True

def test_there_is_another_solution():
    sudoku = [
        [5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]
    ]
    
    original = [fila[:] for fila in sudoku]
    
    solve_sudoku(sudoku)
  
    assert there_is_another_solution(original, sudoku) == False


###############################################################


def test_es_valido_invalido_repeticion_fila():
    # Dos 5 en la primera fila
    sudoku = [
        [5,5,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]
    ]
    assert es_valido(sudoku) == False

def test_es_valido_invalido_repeticion_columna():
    # Dos 5 en la primera columna
    sudoku = [
        [5,3,0,0,7,0,0,0,0],
        [5,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]
    ]
    assert es_valido(sudoku) == False

def test_es_valido_invalido_repeticion_subcuadricula():
    # Dos 5 en la primera subcuadrícula 3x3
    sudoku = [
        [5,3,0,0,7,0,0,0,0],
        [6,5,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]
    ]
    assert es_valido(sudoku) == False

def test_solve_sudoku_sin_solucion():
    # Tablero sin solución (imposible)
    sudoku = [
        [1,2,3,4,5,6,7,8,9],
        [4,5,6,7,8,9,1,2,3],
        [7,8,9,1,2,3,4,5,6],
        [2,1,4,3,6,5,8,9,7],
        [3,6,5,8,9,7,2,1,4],
        [8,9,7,2,1,4,3,6,5],
        [5,3,1,6,4,2,9,7,8],
        [6,4,2,9,7,8,5,3,1],
        [9,7,8,5,3,1,6,4,2]
    ]
    # Este tablero ya está lleno pero es inválido (repeticiones)
    assert solve_sudoku(sudoku) == False
