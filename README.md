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

```

# Instalación 

## 1. Clonar el repositorio

```python
!git clone https://github.com/Calambres199/Sudoku
```

---

## 2. Entrar a la carpeta del proyecto

```python
%cd Sudoku
```

---

## 3. Instalar el paquete

```python
!pip install .
```

---

# Uso del paquete

## Importar funciones

```python
from sudoku_pkg.sudoku import (
    is_valid,
    solve_sudoku,
    there_is_another_solution,
    print_grid
)
```

---

# Ejemplo de Sudoku

Los ceros representan casillas vacías.

```python
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
```

---

# Verificar si el Sudoku es válido

```python
is_valid(sudoku)
```

Salida esperada:

```python
True
```

---

# Resolver el Sudoku

```python
solve_sudoku(sudoku)
```

---

# Mostrar solución

```python
print_grid(sudoku)
```

Salida:

```python
5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9
```

---

# Verificar si existe otra solución

```python
there_is_another_solution(original, sudoku)
```

Salida esperada:

```python
No hay otra solución
False
```

---

# Ejemplos de Sudokus inválidos

El paquete detecta automáticamente:

- Repeticiones en filas
- Repeticiones en columnas
- Repeticiones en subcuadrículas

Ejemplo:

```python
sudoku = [
    [5,5,0,0,7,0,0,0,0],
    ...
]
```

```python
is_valid(sudoku)
```

Salida:

```python
False
```
# Pruebas Pytest

El proyecto también incluye pruebas automáticas usando `pytest`.

```bash
test_sudoku.py
```

Para ejecutarlas:

```python
!pip install pytest
!pytest
```
---

# Cuaderno interactivo de ejemplos
El repositorio incluye un cuaderno de Jupyter con distintos ejemplos para aprender a utilizar el paquete:

```bash
Ejemplos.ipynb
```

# Autores
Bautista Romero Arizbeth Guadalupe
S\'anchez Mart\'inez Jared

Proyecto desarrollado en Python para resolver Sudokus mediante técnicas de búsqueda y validación lógica.
