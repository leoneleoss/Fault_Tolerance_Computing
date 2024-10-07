import httpx
from prefect import flow, task
import asyncio
import sqlite3
import os

# Obtener el directorio del script
current_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(current_dir, 'todos.db')

# Tarea para obtener múltiples TODOs de la API usando httpx
@task(retries=3, retry_delay_seconds=10)
async def fetch_todos_from_api():
    url = "https://jsonplaceholder.cypress.io/todos"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    
    if response.status_code != 200:
        raise Exception(f"Error al obtener datos de la API: {response.status_code}")
    
    todos = response.json()
    print("\n")
    for i, todo in enumerate(todos[:3]):
        print(f"Datos del TODO {i+1}:\n{todo}")
    print("\n  . . . \n")
    return todos

# Tarea para filtrar TODOs completados
@task
def filter_completed_todos(todos):
    completed_todos = [todo for todo in todos if todo['completed']]
    print("\n")
    print(f"Se encontraron {len(completed_todos)} TODOs completados.")
    print("\n")
    return completed_todos

# Tarea para almacenar los TODOs completados en una base de datos SQLite
@task
def store_completed_todos_in_db(completed_todos):
    # Conectar a la base de datos SQLite (se creará si no existe)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Crear la tabla si no existe
    cursor.execute('''CREATE TABLE IF NOT EXISTS completed_todos (
        id INTEGER PRIMARY KEY,
        userId INTEGER,
        title TEXT,
        completed BOOLEAN
    )''')

    # Insertar los TODOs completados en la base de datos
    for todo in completed_todos:
        cursor.execute('''INSERT OR REPLACE INTO completed_todos (id, userId, title, completed)
                          VALUES (?, ?, ?, ?)''', 
                       (todo['id'], todo['userId'], todo['title'], todo['completed']))

    # Guardar cambios y cerrar conexión
    conn.commit()
    conn.close()
    print(f"\nCargadas {len(completed_todos)} tareas completadas en la base de datos.\n")

# Tarea para generar un reporte de los TODOs completados
@task
def generate_completed_todos_report(completed_todos):
    print("\n")
    print("Generando reporte de TODOs completados:")
    for todo in completed_todos:
        print(f"- TODO '{todo['title']}' (ID: {todo['id']}) está completado.")

# Definición del flujo usando la nueva API de Prefect
@flow
async def todo_pipeline():
    # Obtener los datos de los TODOs desde la API
    todos = await fetch_todos_from_api()

    # Filtrar los TODOs completados
    completed_todos = filter_completed_todos(todos)

    # Almacenar los TODOs completados en la base de datos
    store_completed_todos_in_db(completed_todos)

    # Generar un reporte con los TODOs completados
    generate_completed_todos_report(completed_todos)

# Ejecuta el flujo
if __name__ == "__main__":
    asyncio.run(todo_pipeline())  # Ejecuta el flujo usando asyncio
