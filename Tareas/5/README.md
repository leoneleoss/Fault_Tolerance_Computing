
# Calculadora con Estado

Esta es una calculadora simple construida con Python y Tkinter, que no solo realiza operaciones matemáticas básicas, sino que también muestra el estado de la aplicación en tiempo real utilizando programación con hilos. 

![Ejecución deL Código: ](Ejecucion.png)

## Funcionalidades

- Operaciones matemáticas básicas: suma, resta, multiplicación, división.
- Funciones avanzadas: raíz cuadrada, seno, coseno, tangente.
- Funcionalidades de limpieza: botones para borrar la entrada actual (`C`), borrar la última entrada (`CE`), y retroceder un carácter (`<--`).
- Estado de la aplicación mostrado en la interfaz y en la terminal.

## Implementación de Hilos

La programación con hilos se utiliza en esta aplicación para permitir que el estado de la calculadora se imprima en la terminal sin bloquear la interfaz gráfica de usuario. Aquí se detallan las partes clave de la implementación:

### 1. Hilo para Monitorear el Estado

Se define una función `revisar_estado_terminal()` que se ejecuta en un hilo separado. Esta función se encarga de imprimir el estado actual de la calculadora en la terminal cada dos segundos.

```python
def revisar_estado_terminal():
    global estado_global
    while True:
        print(f"[Terminal] Estado de la aplicación: {estado_global}")
        time.sleep(2)  # Cada 2 segundos imprime el estado actual en la terminal
```

### 2. Uso de `threading`

Un hilo se inicia antes de entrar en el bucle principal de la interfaz gráfica, permitiendo que la función de revisión de estado se ejecute de manera concurrente con la interacción del usuario:

```python
# Iniciar el hilo para monitorear el estado en la terminal
hilo_terminal = threading.Thread(target=revisar_estado_terminal)
hilo_terminal.daemon = True  # Hilo como demonio, se cierra al terminar la aplicación
hilo_terminal.start()
```

### 3. Estados de la Aplicación

La variable `estado_global` se utiliza para mantener el estado actual de la calculadora. Este estado se actualiza en función de las acciones del usuario (por ejemplo, al realizar una operación, al limpiar la entrada, etc.):

```python
estado_global = "Calculadora Iniciada"

# Ejemplo de actualización de estado
estado_global = "Calculando..."
```

Esto permite que los usuarios tengan información constante sobre lo que está sucediendo en la aplicación, tanto en la interfaz de usuario como en la terminal, sin afectar el rendimiento o la usabilidad de la calculadora.
