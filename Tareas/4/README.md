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
    Running threads...
    [2024-09-16 12:00:00] Thread-0: Starting to count letters in file_1.txt
    [2024-09-16 12:00:00] Thread-1: Starting to count letters in file_2.txt
    ...

    Running processes...
    [2024-09-16 12:00:10] Process-0: Starting to count letters in file_1.txt
    [2024-09-16 12:00:10] Process-1: Starting to count letters in file_2.txt
    ...

    Running asyncio tasks...
    [2024-09-16 12:00:20] Async-0: Starting to count letters in file_1.txt
    [2024-09-16 12:00:20] Async-1: Starting to count letters in file_2.txt
    ...
```
