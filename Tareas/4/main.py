import threading
import multiprocessing
import asyncio
import os
import time
import datetime


# Crear archivos de texto de ejemplo dentro de una carpeta
def create_text_files(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

    texts = ["This is the first file.\nIt has some content.",
             "This is the second file.\nAnother content here.",
             "Yet another file with different content.",
             "A fourth file just for testing purposes."]

    for i, text in enumerate(texts):
        with open(os.path.join(directory, f'file_{i+1}.txt'), 'w') as f:
            f.write(text)


# Función para contar letras en un archivo con hilos
def thread_count_letters(file_name, thread_id):
    start_time = datetime.datetime.now()
    print(f"[{start_time}] Thread-{thread_id}: Starting to count letters in {file_name}")

    print(f"Thread-{thread_id} is working...\n")


    with open(file_name, 'r') as f:
        content = f.read()
    letter_count = sum(1 for char in content if char.isalpha())

    end_time = datetime.datetime.now()
    print(f"[{end_time}] Thread-{thread_id}: Finished. {file_name} has {letter_count} letters.\n")


# Función para contar letras con procesos
def process_count_letters(file_name, process_id):
    start_time = datetime.datetime.now()
    print(f"[{start_time}] Process-{process_id}: Starting to count letters in {file_name}")

    print(f"Process-{process_id} is working...\n")


    with open(file_name, 'r') as f:
        content = f.read()
    letter_count = sum(1 for char in content if char.isalpha())
    end_time = datetime.datetime.now()
    print(f"[{end_time}] Process-{process_id}: Finished. {file_name} has {letter_count} letters.\n")


# Función para contar letras con asyncio
async def async_count_letters(file_name, task_id):
    start_time = datetime.datetime.now()

    print(f"[{start_time}] Async-{task_id}: Starting to count letters in {file_name}")

    print(f"Async-{task_id} is working...\n")


    with open(file_name, 'r') as f:
        content = f.read()
    letter_count = sum(1 for char in content if char.isalpha())

    end_time = datetime.datetime.now()
    print(f"[{end_time}] Async-{task_id}: Finished. {file_name} has {letter_count} letters.\n")


# Ejecutar múltiples hilos
def run_threads(files):
    print("\n\n\n==== Running threads ====\n")
    start_time = time.time()
    
    threads = []
    for i, file in enumerate(files):
        thread = threading.Thread(target=thread_count_letters, args=(file, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"\n==== Threads completed in {end_time - start_time} seconds ====\n")
    print("Note: Threads use the same core.")


# Ejecutar múltiples procesos
def run_processes(files):
    print("\n\n\n==== Running processes ====\n")
    start_time = time.time()

    processes = []
    for i, file in enumerate(files):
        process = multiprocessing.Process(target=process_count_letters, args=(file, i))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    end_time = time.time()
    print(f"\n==== Processes completed in {end_time - start_time} seconds ====\n")
    cpu_count = multiprocessing.cpu_count()
    print(f"Note: Processes utilized {len(processes)} cores out of {cpu_count} available cores.")


# Ejecutar múltiples tareas asíncronas
async def run_asyncio_tasks(files):
    print("\n\n\n==== Running asyncio tasks ====\n")
    start_time = time.time()
    
    await asyncio.gather(*(async_count_letters(file, i) for i, file in enumerate(files)))

    end_time = time.time()
    print(f"\n==== Asyncio tasks completed in {end_time - start_time} seconds ====\n")
    print("Note: Asyncio uses a single core.")


# Función principal que ejecuta las diferentes tareas
def main():

    # Directorio donde se crearán los archivos
    directory = input(r"Ruta del archivo: ")

    # Crear archivos de texto de ejemplo
    create_text_files(directory)

    files = [os.path.join(directory, f'file_{i+1}.txt') for i in range(4)]

    print("==== Starting all tasks ====\n")

    # Mostrar información sobre la CPU
    cpu_count = multiprocessing.cpu_count()
    print(f"Number of CPU cores: {cpu_count}")

    # Ejecutar hilos
    run_threads(files)

    # Ejecutar procesos
    run_processes(files)

    # Ejecutar tareas asíncronas
    asyncio.run(run_asyncio_tasks(files))

    print("\n==== All tasks completed ====\n")


if __name__ == "__main__":
    main()
