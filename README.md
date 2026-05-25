# Sudoku Resolver

## Descripción general

Este proyecto implementa una biblioteca en Python para la resolución de Sudokus 9×9 mediante el algoritmo de **backtracking** (búsqueda con retroceso).

El objetivo principal es:

- Resolver cualquier Sudoku 9×9 válido
- Verificar si un tablero es válido (sin repeticiones en filas, columnas o subcuadrículas)
- Determinar si la solución encontrada es única

La biblioteca fue desarrollada utilizando buenas prácticas de programación en Python:

- Modularización
- Documentación con docstrings
- Pruebas unitarias con `pytest`
- Notebook de ejemplos de uso

---

# El problema del Sudoku

El Sudoku es un rompecabezas que consiste en una cuadrícula de 9×9 celdas, dividida en 9 subcuadrículas de 3×3. Algunas celdas contienen números fijos (pistas) y el resto están vacías.

El objetivo es llenar las celdas vacías con dígitos del 1 al 9 cumpliendo tres reglas simples:

1. **Cada fila** debe contener todos los números del 1 al 9 sin repetir.
2. **Cada columna** debe contener todos los números del 1 al 9 sin repetir.
3. **Cada subcuadrícula** de 3×3 debe contener todos los números del 1 al 9 sin repetir.

---

# Algoritmo de backtracking

El algoritmo de backtracking (búsqueda con retroceso) funciona de la siguiente manera:

1. Busca la primera celda vacía en el tablero
2. Prueba números del 1 al 9 en esa celda
3. Antes de asignar un número, verifica que no esté ya en la misma fila, columna o subcuadrícula
4. Si el número es válido, lo asigna y llama recursivamente a la función para la siguiente celda vacía
5. Si más adelante no se puede completar el tablero (ningún número funciona en alguna celda), retrocede a la celda anterior y prueba el siguiente número
6. El proceso termina cuando todas las celdas están llenas (solución encontrada) o se determina que no hay solución

### Ventajas del backtracking

- **Poda temprana**: descarta ramas inválidas antes de explorarlas por completo
- **Garantía de solución**: encuentra la solución si existe
- **Bajo uso de memoria**: solo necesita el tablero y la pila de recursión

---

# Funciones implementadas

| Función | Descripción |
|---------|-------------|
| `print_grid(arr)` | Imprime el tablero en formato legible 9×9. |
| `find_empty_location(arr, l)` | Busca la primera celda vacía en el tablero. |
| `used_in_row(arr, row, num)` | Verifica si un número ya existe en una fila. |
| `used_in_col(arr, col, num)` | Verifica si un número ya existe en una columna. |
| `used_in_box(arr, row, col, num)` | Verifica si un número ya existe en una subcuadrícula 3×3. |
| `check_location_is_safe(arr, row, col, num)` | Verifica si es seguro colocar un número en una celda. |
| `es_valido(tablero)` | Verifica si un tablero inicial es válido. |
| `solve_sudoku(arr)` | Resuelve el Sudoku usando backtracking. |
| `there_is_another_solution(original, solucion)` | Determina si el Sudoku tiene más de una solución. |

---

# Estructura del proyecto

```text
Sudoku/
│
├── sudoku_pkg/
│   ├── __init__.py
│   └── sudoku.py
│
├── tests/
│   └── test_sudoku.py
│
├── Ejemplos.ipynb
├── README.md
└── pyproject.toml
