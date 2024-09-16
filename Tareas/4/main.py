import threading
import multiprocessing
import asyncio
import time
import datetime

# Crear archivos de texto de ejemplo
def create_text_files():
    texts = ["This is the first file.\nIt has some content.",
             "This is the second file.\nAnother content here.",
             "Yet another file with different content.",
             "A fourth file just for testing purposes."]
    
    for i, text in enumerate(texts):
        with open(f'file_{i+1}.txt', 'w') as f:
            f.write(text)

# Función para contar letras en un archivo con hilos
def thread_count_letters(file_name, thread_id):
    start_time = datetime.datetime.now()
    print(f"[{start_time}] Thread-{thread_id}: Starting to count letters in {file_name}")
    time.sleep(3)  # Simular trabajo con mayor tiempo
    with open(file_name, 'r') as f:
        content = f.read()
    letter_count = sum(1 for char in content if char.isalpha())
    end_time = datetime.datetime.now()
    print(f"[{end_time}] Thread-{thread_id}: {file_name} has {letter_count} letters.")

# Función para contar letras con procesos
def process_count_letters(file_name, process_id):
    start_time = datetime.datetime.now()
    print(f"[{start_time}] Process-{process_id}: Starting to count letters in {file_name}")
    time.sleep(4)  # Simular trabajo con mayor tiempo
    with open(file_name, 'r') as f:
        content = f.read()
    letter_count = sum(1 for char in content if char.isalpha())
    end_time = datetime.datetime.now()
    print(f"[{end_time}] Process-{process_id}: {file_name} has {letter_count} letters.")

# Función para contar letras con asyncio
async def async_count_letters(file_name, task_id):
    start_time = datetime.datetime.now()
    print(f"[{start_time}] Async-{task_id}: Starting to count letters in {file_name}")
    await asyncio.sleep(2)  # Simular trabajo asíncrono con mayor tiempo
    with open(file_name, 'r') as f:
        content = f.read()
    letter_count = sum(1 for char in content if char.isalpha())
    end_time = datetime.datetime.now()
    print(f"[{end_time}] Async-{task_id}: {file_name} has {letter_count} letters.")

# Ejecutar múltiples hilos
def run_threads(files):
    threads = []
    for i, file in enumerate(files):
        thread = threading.Thread(target=thread_count_letters, args=(file, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

# Ejecutar múltiples procesos
def run_processes(files):
    processes = []
    for i, file in enumerate(files):
        process = multiprocessing.Process(target=process_count_letters, args=(file, i))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

# Ejecutar múltiples tareas asíncronas
async def run_asyncio_tasks(files):
    await asyncio.gather(*(async_count_letters(file, i) for i, file in enumerate(files)))

# Función principal que ejecuta las diferentes tareas
def main():
    # Crear archivos de texto de ejemplo
    create_text_files()

    files = [f'file_{i+1}.txt' for i in range(4)]

    print("Running threads...")
    run_threads(files)

    print("\nRunning processes...")
    run_processes(files)

    print("\nRunning asyncio tasks...")
    asyncio.run(run_asyncio_tasks(files))

if __name__ == "__main__":
    main()
