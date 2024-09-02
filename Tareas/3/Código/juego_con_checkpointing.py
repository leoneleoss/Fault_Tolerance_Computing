import pickle
import os
import random

# Definir el nombre del archivo para el punto de control
archivo_checkpoint = 'checkpoint_juego.pkl'

# Función para guardar el estado
def guardar_checkpoint(estado):
    with open(archivo_checkpoint, 'wb') as f:
        pickle.dump(estado, f)
    print(f"Punto de control guardado: Posición del jugador {estado['jugador_pos']}")

# Función para cargar el estado
def cargar_checkpoint():
    if os.path.exists(archivo_checkpoint):
        with open(archivo_checkpoint, 'rb') as f:
            estado = pickle.load(f)
        print(f"Punto de control cargado: Posición del jugador {estado['jugador_pos']}")
        return estado
    else:
        return None

# Función para mostrar el tablero de juego
def mostrar_tablero(estado):
    for y in range(estado['alto']):
        for x in range(estado['ancho']):
            if (x, y) == estado['jugador_pos']:
                print("J", end=" ")  # Posición del jugador
            elif (x, y) in estado['objetos']:
                print("O", end=" ")  # Objeto
            elif (x, y) in estado['obstaculos']:
                print("X", end=" ")  # Obstáculo
            else:
                print(".", end=" ")  # Espacio vacío
        print()
    print()

# Función para mover al jugador
def mover_jugador(estado, direccion):
    x, y = estado['jugador_pos']
    if direccion == 'w' and y > 0:
        y -= 1
    elif direccion == 's' and y < estado['alto'] - 1:
        y += 1
    elif direccion == 'a' and x > 0:
        x -= 1
    elif direccion == 'd' and x < estado['ancho'] - 1:
        x += 1
    else:
        print("Movimiento no permitido.")
        return

    nueva_pos = (x, y)

    if nueva_pos in estado['obstaculos']:
        print("¡Chocaste con un obstáculo! Juego terminado.")
        exit()
    elif nueva_pos in estado['objetos']:
        estado['objetos'].remove(nueva_pos)
        print("¡Objeto recogido!")

    estado['jugador_pos'] = nueva_pos

def iniciar_juego():
    # Configuración inicial del juego
    ancho = 5
    alto = 5
    jugador_pos = (0, 0)
    objetos = [(random.randint(1, ancho-1), random.randint(1, alto-1)) for _ in range(3)]
    obstaculos = [(random.randint(1, ancho-1), random.randint(1, alto-1)) for _ in range(3)]

    # Evitar que los objetos y obstáculos se superpongan con el jugador
    objetos = [obj for obj in objetos if obj != jugador_pos]
    obstaculos = [obs for obs in obstaculos if obs != jugador_pos]

    estado_inicial = {
        'ancho': ancho,
        'alto': alto,
        'jugador_pos': jugador_pos,
        'objetos': objetos,
        'obstaculos': obstaculos
    }

    return estado_inicial

if __name__ == "__main__":
    # Intentar cargar un punto de control previo
    estado = cargar_checkpoint()
    
    # Si no se encuentra un punto de control, inicializar el juego
    if estado is None:
        estado = iniciar_juego()
    
    # Bucle principal del juego
    while True:
        mostrar_tablero(estado)
        movimiento = input("Mover (w/a/s/d) o salir (q): ").lower()
        
        if movimiento == 'q':
            print("Saliendo del juego...")
            guardar_checkpoint(estado)
            break
        elif movimiento in ['w', 'a', 's', 'd']:
            mover_jugador(estado, movimiento)
            guardar_checkpoint(estado)  # Guardar después de cada movimiento
        else:
            print("Entrada no válida. Intente de nuevo.")
