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

```bash yaml
PS C:\Users\leoba\OneDrive\Documentos\GitHub\Fault_Tolerance_Computing> & C:/Users/leoba/AppData/Local/Programs/Python/Python312/python.exe c:/Users/leoba/OneDrive/Documentos/GitHub/Fault_Tolerance_Computing/Tareas/4/main.py
Ruta del archivo: C:\Users\leoba\OneDrive\Documentos\GitHub\Fault_Tolerance_Computing\Tareas\4
==== Starting all tasks ====


==== Running threads ====

[2024-09-23 10:19:15.002575] Thread-0: Starting to count letters in C:\Users\leoba\OneDrive\Documentos\GitHub\Fault_Tolerance_Computing\Tareas\4\file_1.txt
[2024-09-23 10:19:15.002575] Thread-1: Starting to count letters in C:\Users\leoba\OneDrive\Documentos\GitHub\Fault_Tolerance_Computing\Tareas\4\file_2.txt
[2024-09-23 10:19:15.002575] Thread-2: Starting to count letters in C:\Users\leoba\OneDrive\Documentos\GitHub\Fault_Tolerance_Computing\Tareas\4\file_3.txt
[2024-09-23 10:19:15.002575] Thread-3: Starting to count letters in C:\Users\leoba\OneDrive\Documentos\GitHub\Fault_Tolerance_Computing\Tareas\4\file_4.txt
Thread-0 is working...
Thread-3 is working...
Thread-2 is working...
Thread-1 is working...
[2024-09-23 10:19:29.003702] Thread-3: Finished. C:\Users\leoba\OneDrive\Documentos\GitHub\Fault_Tolerance_Computing\Tareas\4\file_4.txt has 33 letters.

[2024-09-23 10:19:29.004851] Thread-1: Finished. C:\Users\leoba\OneDrive\Documentos\GitHub\Fault_Tolerance_Computing\Tareas\4\file_2.txt has 37 letters.

[2024-09-23 10:19:29.006854] Thread-0: Finished. C:\Users\leoba\OneDrive\Documentos\GitHub\Fault_Tolerance_Computing\Tareas\4\file_1.txt has 34 letters.

[2024-09-23 10:19:29.007856] Thread-2: Finished. C:\Users\leoba\OneDrive\Documentos\GitHub\Fault_Tolerance_Computing\Tareas\4\file_3.txt has 34 letters.


==== Running processes ====

[2024-09-23 10:19:29.103943] Process-0: Starting to count letters in C:\Users\leoba\OneDrive\Documentos\GitHub\Fault_Tolerance_Computing\Tareas\4\file_1.txt
[2024-09-23 10:19:29.106946] Process-1: Starting to count letters in C:\Users\leoba\OneDrive\Documentos\GitHub\Fault_Tolerance_Computing\Tareas\4\file_2.txt
[2024-09-23 10:19:29.106946] Process-2: Starting to count letters in C:\Users\leoba\OneDrive\Documentos\GitHub\Fault_Tolerance_Computing\Tareas\4\file_3.txt
[2024-09-23 10:19:29.110949] Process-3: Starting to count letters in C:\Users\leoba\OneDrive\Documentos\GitHub\Fault_Tolerance_Computing\Tareas\4\file_4.txt
Process-0 is working...
Process-1 is working...
Process-2 is working...
Process-3 is working...
[2024-09-23 10:19:44.106569] Process-0: Finished. C:\Users\leoba\OneDrive\Documentos\GitHub\Fault_Tolerance_Computing\Tareas\4\file_1.txt has 34 letters.

[2024-09-23 10:19:44.107432] Process-1: Finished. C:\Users\leoba\OneDrive\Documentos\GitHub\Fault_Tolerance_Computing\Tareas\4\file_2.txt has 37 letters. 

[2024-09-23 10:19:44.108428] Process-2: Finished. C:\Users\leoba\OneDrive\Documentos\GitHub\Fault_Tolerance_Computing\Tareas\4\file_3.txt has 34 letters. 

[2024-09-23 10:19:44.111430] Process-3: Finished. C:\Users\leoba\OneDrive\Documentos\GitHub\Fault_Tolerance_Computing\Tareas\4\file_4.txt has 33 letters. 


==== Running asyncio tasks ====

[2024-09-23 10:19:44.122441] Async-0: Starting to count letters in C:\Users\leoba\OneDrive\Documentos\GitHub\Fault_Tolerance_Computing\Tareas\4\file_1.txt
[2024-09-23 10:19:44.122441] Async-1: Starting to count letters in C:\Users\leoba\OneDrive\Documentos\GitHub\Fault_Tolerance_Computing\Tareas\4\file_2.txt
[2024-09-23 10:19:44.122441] Async-2: Starting to count letters in C:\Users\leoba\OneDrive\Documentos\GitHub\Fault_Tolerance_Computing\Tareas\4\file_3.txt
[2024-09-23 10:19:44.122441] Async-3: Starting to count letters in C:\Users\leoba\OneDrive\Documentos\GitHub\Fault_Tolerance_Computing\Tareas\4\file_4.txt
Async-0 is working...
Async-2 is working...
Async-1 is working...
Async-3 is working...
[2024-09-23 10:19:59.123846] Async-0: Finished. C:\Users\leoba\OneDrive\Documentos\GitHub\Fault_Tolerance_Computing\Tareas\4\file_1.txt has 34 letters.

[2024-09-23 10:19:59.123846] Async-1: Finished. C:\Users\leoba\OneDrive\Documentos\GitHub\Fault_Tolerance_Computing\Tareas\4\file_2.txt has 37 letters.

[2024-09-23 10:19:59.124846] Async-2: Finished. C:\Users\leoba\OneDrive\Documentos\GitHub\Fault_Tolerance_Computing\Tareas\4\file_3.txt has 34 letters.

[2024-09-23 10:19:59.124846] Async-3: Finished. C:\Users\leoba\OneDrive\Documentos\GitHub\Fault_Tolerance_Computing\Tareas\4\file_4.txt has 33 letters.


==== All tasks completed ====
```
