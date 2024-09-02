# Juego de Consola con Checkpointing en Python

Este repositorio contiene un simple juego de consola implementado en Python que demuestra el uso de la técnica de checkpointing para guardar y restaurar el estado del juego. El juego se desarrolla en una cuadrícula 2D donde el jugador puede moverse, recoger objetos y evitar obstáculos. El estado del juego se guarda automáticamente después de cada movimiento, permitiendo que el jugador reanude el juego desde el último punto guardado en caso de cierre o interrupción.

## Juego
  [Código en Google Collab](https://colab.research.google.com/drive/1VQiZ1qQxZpHszk8AWhMbbtwIf44ASxpX?usp=sharing)

## Características

- **Juego en consola**: Movimiento del jugador en una cuadrícula 2D usando las teclas `w`, `a`, `s`, `d`.
- **Objetos y obstáculos**: Objetos que el jugador puede recoger y obstáculos que deben evitarse.
- **Checkpointing**: Guarda automáticamente el estado del juego en un archivo después de cada movimiento.
- **Reanudación**: Carga automáticamente el último estado guardado cuando se reinicia el juego.

## Requisitos

- Python 3.x

## Instalación

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/tuusuario/juego-con-checkpointing.git
   cd juego-con-checkpointing
   ```
2.  **Ejecuta el juego:**
   ```bash
    python juego_con_checkpointing.py
   ```
## Cómo Jugar
1. **Inicio del juego:**
    El jugador comienza en la esquina superior izquierda de una cuadrícula 5x5.
3. **Controles:**
  - w: Mover hacia arriba.
  - a: Mover hacia la izquierda.
  - s: Mover hacia abajo.
  - d: Mover hacia la derecha.
  - q: Salir del juego y guardar el estado actual.
3. **Objetivos:**
- Recoge todos los objetos (O) moviéndote sobre ellos.
- Evita los obstáculos (X). Si el jugador choca con un obstáculo, el juego termina.
4. **Guardar y Cargar:**
  El juego guarda automáticamente el estado después de cada movimiento. Si el juego se interrumpe o el jugador sale con q, se puede reanudar desde el último estado guardado ejecutando el juego de nuevo.

## Estructura del Código
### Funciones Principales

- `guardar_checkpoint(estado)`:
 Guarda el estado actual del juego en un archivo utilizando el módulo pickle.
- `cargar_checkpoint()`:
 Carga el estado del juego desde un archivo si existe, permitiendo la reanudación del juego.
- `mostrar_tablero(estado)`:
 Muestra el tablero de juego en la consola, indicando la posición del jugador, los objetos y los obstáculos.
- `mover_jugador(estado, direccion)`:
 Mueve al jugador en la dirección especificada (si es válida) y actualiza el estado del juego.
- `iniciar_juego()`:
 Configura y devuelve el estado inicial del juego, con el jugador en la posición inicial y los objetos y obstáculos colocados aleatoriamente.

## Autor
- Leobardo Leonel Cortés Pérez - [Leonel Cortés](https://github.com/leoneleoss)
