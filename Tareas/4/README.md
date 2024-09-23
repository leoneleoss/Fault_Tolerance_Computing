# Concurrent Letter Counting

Este programa en Python demuestra el uso de concurrencia y paralelismo mediante hilos (`threading`), procesos (`multiprocessing`) y tareas asíncronas (`asyncio`). Cada mecanismo de concurrencia se utiliza para contar letras en varios archivos de texto de manera paralela.

## Funcionalidad

1. **Creación de Archivos:** Se generan cuatro archivos de texto con contenido de ejemplo.
2. **Conteo de Letras:**
   - **Hilos:** Usa hilos para contar letras en cada archivo.
   - **Procesos:** Usa procesos para contar letras en cada archivo.
   - **Asyncio:** Usa tareas asíncronas para contar letras en cada archivo.

## Requisitos

- Python 3.7 o superior

## Instalación

No se requieren dependencias adicionales fuera de la biblioteca estándar de Python.

## Uso

1. **Ejecuta el script:**
  ```bash python
    concurrent_letter_counting.py
  ```

2. **Observa la salida:** Verás información detallada en la terminal sobre el inicio y fin de cada tarea, identificando claramente qué tareas están corriendo simultáneamente.
Detalles del Código

## Detalles del código

`create_text_files():` Crea archivos de texto de ejemplo.
`thread_count_letters(file_name, thread_id):` Cuenta letras en un archivo usando hilos.
`process_count_letters(file_name, process_id):` Cuenta letras en un archivo usando procesos.
`async_count_letters(file_name, task_id):` Cuenta letras en un archivo usando asyncio.
`run_threads(files):` Ejecuta tareas de conteo con hilos.
`run_processes(files):` Ejecuta tareas de conteo con procesos.
`run_asyncio_tasks(files):` Ejecuta tareas de conteo asíncronas.
`main():` Función principal que coordina la ejecución de todas las tareas.

## Ejemplo de Salida

El código proporciona información sobre cómo cada enfoque maneja la concurrencia (hilos, procesos y asincronía) en relación con los núcleos de CPU disponibles, permitiendo observar mejor sus diferencias y cómo se aprovechan los recursos del sistema. 

```bash 
Ruta del archivo: C:\Users\leoba\OneDrive\Documentos\GitHub\Fault_Tolerance_Computing\Tareas\4
==== Starting all tasks ====

Number of CPU cores: 12



==== Running threads ====

[2024-09-23 10:48:22.295895] Thread-0: Starting to count letters in C:\Users\leoba\OneDrive\Documentos\GitHub\Fault_Tolerance_Computing\Tareas\4\file_1.txt
Thread-0 is working...
[2024-09-23 10:48:22.296896] Thread-1: Starting to count letters in C:\Users\leoba\OneDrive\Documentos\GitHub\Fault_Tolerance_Computing\Tareas\4\file_2.txt

Thread-1 is working...
[2024-09-23 10:48:22.296896] Thread-3: Starting to count letters in C:\Users\leoba\OneDrive\Documentos\GitHub\Fault_Tolerance_Computing\Tareas\4\file_4.txt

Thread-3 is working...

[2024-09-23 10:48:22.296896] Thread-2: Starting to count letters in C:\Users\leoba\OneDrive\Documentos\GitHub\Fault_Tolerance_Computing\Tareas\4\file_3.txt
Thread-2 is working...

[2024-09-23 10:48:22.297897] Thread-0: Finished. C:\Users\leoba\OneDrive\Documentos\GitHub\Fault_Tolerance_Computing\Tareas\4\file_1.txt has 34 letters.   
[2024-09-23 10:48:22.297897] Thread-1: Finished. C:\Users\leoba\OneDrive\Documentos\GitHub\Fault_Tolerance_Computing\Tareas\4\file_2.txt has 37 letters.   


[2024-09-23 10:48:22.297897] Thread-3: Finished. C:\Users\leoba\OneDrive\Documentos\GitHub\Fault_Tolerance_Computing\Tareas\4\file_4.txt has 33 letters.   

[2024-09-23 10:48:22.297897] Thread-2: Finished. C:\Users\leoba\OneDrive\Documentos\GitHub\Fault_Tolerance_Computing\Tareas\4\file_3.txt has 34 letters.   


==== Threads completed in 0.0020017623901367188 seconds ====

Note: Threads use the same core.



==== Running processes ====

[2024-09-23 10:48:22.397989] Process-0: Starting to count letters in C:\Users\leoba\OneDrive\Documentos\GitHub\Fault_Tolerance_Computing\Tareas\4\file_1.txt
Process-0 is working...

[2024-09-23 10:48:22.397989] Process-0: Finished. C:\Users\leoba\OneDrive\Documentos\GitHub\Fault_Tolerance_Computing\Tareas\4\file_1.txt has 34 letters.   

[2024-09-23 10:48:22.399990] Process-1: Starting to count letters in C:\Users\leoba\OneDrive\Documentos\GitHub\Fault_Tolerance_Computing\Tareas\4\file_2.txt
Process-1 is working...

[2024-09-23 10:48:22.399990] Process-1: Finished. C:\Users\leoba\OneDrive\Documentos\GitHub\Fault_Tolerance_Computing\Tareas\4\file_2.txt has 37 letters.   

[2024-09-23 10:48:22.401991] Process-2: Starting to count letters in C:\Users\leoba\OneDrive\Documentos\GitHub\Fault_Tolerance_Computing\Tareas\4\file_3.txt
Process-2 is working...

[2024-09-23 10:48:22.401991] Process-2: Finished. C:\Users\leoba\OneDrive\Documentos\GitHub\Fault_Tolerance_Computing\Tareas\4\file_3.txt has 34 letters.

[2024-09-23 10:48:22.404994] Process-3: Starting to count letters in C:\Users\leoba\OneDrive\Documentos\GitHub\Fault_Tolerance_Computing\Tareas\4\file_4.txt
Process-3 is working...

[2024-09-23 10:48:22.404994] Process-3: Finished. C:\Users\leoba\OneDrive\Documentos\GitHub\Fault_Tolerance_Computing\Tareas\4\file_4.txt has 33 letters.


==== Processes completed in 0.11810755729675293 seconds ====

Note: Processes utilized 4 cores out of 12 available cores.



==== Running asyncio tasks ====

[2024-09-23 10:48:22.417006] Async-0: Starting to count letters in C:\Users\leoba\OneDrive\Documentos\GitHub\Fault_Tolerance_Computing\Tareas\4\file_1.txt
Async-0 is working...

[2024-09-23 10:48:22.418006] Async-0: Finished. C:\Users\leoba\OneDrive\Documentos\GitHub\Fault_Tolerance_Computing\Tareas\4\file_1.txt has 34 letters.

[2024-09-23 10:48:22.418006] Async-1: Starting to count letters in C:\Users\leoba\OneDrive\Documentos\GitHub\Fault_Tolerance_Computing\Tareas\4\file_2.txt
Async-1 is working...

[2024-09-23 10:48:22.418006] Async-1: Finished. C:\Users\leoba\OneDrive\Documentos\GitHub\Fault_Tolerance_Computing\Tareas\4\file_2.txt has 37 letters.

[2024-09-23 10:48:22.418006] Async-2: Starting to count letters in C:\Users\leoba\OneDrive\Documentos\GitHub\Fault_Tolerance_Computing\Tareas\4\file_3.txt
Async-2 is working...

[2024-09-23 10:48:22.419008] Async-2: Finished. C:\Users\leoba\OneDrive\Documentos\GitHub\Fault_Tolerance_Computing\Tareas\4\file_3.txt has 34 letters.

[2024-09-23 10:48:22.419008] Async-3: Starting to count letters in C:\Users\leoba\OneDrive\Documentos\GitHub\Fault_Tolerance_Computing\Tareas\4\file_4.txt
Async-3 is working...

[2024-09-23 10:48:22.419008] Async-3: Finished. C:\Users\leoba\OneDrive\Documentos\GitHub\Fault_Tolerance_Computing\Tareas\4\file_4.txt has 33 letters.


==== Asyncio tasks completed in 0.003002643585205078 seconds ====

Note: Asyncio uses a single core.

==== All tasks completed ====

```

  
