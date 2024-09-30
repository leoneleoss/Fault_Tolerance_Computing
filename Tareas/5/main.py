import tkinter as tk
import threading
import time
import math

# Variable global para guardar el estado de la calculadora
estado_global = "Calculadora Iniciada"

# Función para revisar y mostrar el estado en la terminal en segundo plano
def revisar_estado_terminal():
    global estado_global
    while True:
        print(f"[Terminal] Estado de la aplicación: {estado_global}")
        time.sleep(2)  # Cada 2 segundos imprime el estado actual en la terminal

# Función que maneja las operaciones de la calculadora
def realizar_operacion(estado_label):
    global estado_global
    try:
        # Actualiza el estado cuando se va a realizar una operación
        estado_label.config(text="Estado: Calculando...", anchor="w")
        estado_global = "Calculando..."

        # Evalúa la operación y muestra el resultado
        result = eval(entry.get())
        
        # Mueve la operación a la memoria y limpia el cuadro de entrada
        memoria_entry.config(state=tk.NORMAL)
        memoria_entry.insert(tk.END, f"{entry.get()} = {result}\n")
        memoria_entry.config(state=tk.DISABLED)

        # Muestra el resultado en el cuadro de entrada
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))

        # Actualiza el estado cuando se realiza la operación correctamente
        estado_label.config(text="Estado: Operación exitosa", anchor="w")
        estado_global = "Operación exitosa"
    except Exception as e:
        # En caso de error, actualiza el estado
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
        estado_label.config(text="Estado: Error en la operación", anchor="w")
        estado_global = "Error en la operación"

# Función que maneja los clics de los botones
def click_boton(valor, estado_label):
    global estado_global
    if valor == "=":
        realizar_operacion(estado_label)
    elif valor == "C":
        # Limpia toda la entrada y actualiza el estado
        entry.delete(0, tk.END)
        estado_label.config(text="Estado: Entrada borrada", anchor="w")
        estado_global = "Entrada borrada"
    elif valor == "CE":
        # Borra la última entrada
        entry.delete(0, tk.END)
        estado_label.config(text="Estado: Entrada actual borrada", anchor="w")
        estado_global = "Entrada actual borrada"
    elif valor == "<--":
        # Borra el último carácter ingresado
        entry.delete(len(entry.get()) - 1)
        estado_label.config(text="Estado: Retroceso ejecutado", anchor="w")
        estado_global = "Retroceso ejecutado"
    elif valor == "√":
        # Calcula la raíz cuadrada
        value = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(math.sqrt(value)))
        estado_label.config(text="Estado: Raíz cuadrada calculada", anchor="w")
        estado_global = "Raíz cuadrada calculada"
    elif valor == "sin":
        # Calcula el seno
        value = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(math.sin(math.radians(value))))
        estado_label.config(text="Estado: Seno calculado", anchor="w")
        estado_global = "Seno calculado"
    elif valor == "cos":
        # Calcula el coseno
        value = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(math.cos(math.radians(value))))
        estado_label.config(text="Estado: Coseno calculado", anchor="w")
        estado_global = "Coseno calculado"
    elif valor == "tan":
        # Calcula la tangente
        value = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(math.tan(math.radians(value))))
        estado_label.config(text="Estado: Tangente calculada", anchor="w")
        estado_global = "Tangente calculada"
    else:
        # Actualiza el estado cuando se ingresa un valor
        estado_label.config(text="Estado: Ingresando datos", anchor="w")
        estado_global = "Ingresando datos"
        entry.insert(tk.END, valor)

# Crear la interfaz de la calculadora
def crear_calculadora():
    global entry, memoria_entry

    root = tk.Tk()
    root.title("Calculadora con Estado")
    
    # Bloquear el tamaño de la ventana
    root.resizable(False, False)

    # Frame para el display y los botones
    main_frame = tk.Frame(root)
    main_frame.pack()

    # Cuadro de entrada para la memoria, arriba del cuadro de entrada
    memoria_entry = tk.Text(main_frame, height=5, width=20, font=('Arial', 12), borderwidth=5, relief="ridge", state=tk.DISABLED)
    memoria_entry.grid(row=0, column=0, columnspan=4, pady=5)

    # Cuadro de entrada para las operaciones
    entry = tk.Entry(main_frame, width=20, font=('Arial', 24), borderwidth=5, relief="ridge")
    entry.grid(row=1, column=0, columnspan=4, pady=5)

    # Botones de la calculadora
    botones = [
        'C', 'CE', '<--',
        '√', 'sin', 'cos', 'tan',
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        '0', '.', '+', '=', 
    ]

    # Colocar la primera fila con solo tres botones
    tk.Button(main_frame, text=botones[0], width=5, height=2, font=('Arial', 18), command=lambda: click_boton(botones[0], estado_label)).grid(row=2, column=0, padx=5, pady=5)
    tk.Button(main_frame, text=botones[1], width=5, height=2, font=('Arial', 18), command=lambda: click_boton(botones[1], estado_label)).grid(row=2, column=1, padx=5, pady=5)
    tk.Button(main_frame, text=botones[2], width=5, height=2, font=('Arial', 18), command=lambda: click_boton(botones[2], estado_label)).grid(row=2, column=2, padx=5, pady=5)

    fila = 3  # Comenzar la fila de botones debajo de los cuadros de entrada
    columna = 0
    
    # Agregar botones a la cuadrícula a partir de la fila 3
    for boton in botones[3:]:  # Ignorar los primeros tres botones
        # Asignamos una acción para cada botón que actualice el estado
        action = lambda x=boton: click_boton(x, estado_label)
        
        # Agregar el botón en la cuadrícula
        tk.Button(main_frame, text=boton, width=5, height=2, font=('Arial', 18), command=action).grid(row=fila, column=columna, padx=5, pady=5)
        
        columna += 1
        # Cambia a la siguiente fila después de 4 botones
        if columna > 3:
            columna = 0
            fila += 1

    # Frame para el estado, colocado en la parte inferior
    estado_frame = tk.Frame(root)
    estado_frame.pack(fill='x')

    # Etiqueta de estado de la aplicación con más espacio
    estado_label = tk.Label(estado_frame, text="Estado: Calculadora Iniciada", font=('Arial', 12), anchor="w")
    estado_label.pack(fill='x', padx=10, pady=5)

    # Iniciar el hilo para monitorear el estado en la terminal
    hilo_terminal = threading.Thread(target=revisar_estado_terminal)
    hilo_terminal.daemon = True  # Hilo como demonio, se cierra al terminar la aplicación
    hilo_terminal.start()

    root.mainloop()

# Ejecutar la calculadora
if __name__ == "__main__":
    crear_calculadora()
