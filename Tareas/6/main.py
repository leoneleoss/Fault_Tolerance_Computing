import httpx
from prefect import flow, task
import asyncio

# Tarea para obtener múltiples TODOs de la API usando httpx
@task(retries=3, retry_delay_seconds=10)
async def fetch_todos_from_api():
    url = "https://jsonplaceholder.cypress.io/todos"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    
    if response.status_code != 200:
        raise Exception(f"Error al obtener datos de la API: {response.status_code}")
    
    todos = response.json()
    print(f"Datos de los TODOs obtenidos: {todos[:2]}")  # Muestra solo los primeros 2 para no sobrecargar
    return todos

# Tarea para filtrar TODOs completados
@task
def filter_completed_todos(todos):
    completed_todos = [todo for todo in todos if todo['completed']]
    print(f"Se encontraron {len(completed_todos)} TODOs completados.")
    return completed_todos

# Tarea para generar un reporte de los TODOs completados
@task
def generate_completed_todos_report(completed_todos):
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

    # Generar un reporte con los TODOs completados
    generate_completed_todos_report(completed_todos)

# Ejecuta el flujo
if __name__ == "__main__":
    asyncio.run(todo_pipeline())  # Ejecuta el flujo usando asyncio
