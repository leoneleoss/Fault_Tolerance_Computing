import httpx
from prefect import flow, task
import asyncio

# Tarea para obtener un TODO de la API usando httpx
@task(retries=3, retry_delay_seconds=10)
async def fetch_todo_from_api():
    url = "https://jsonplaceholder.cypress.io/todos/1"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    
    if response.status_code != 200:
        raise Exception(f"Error al obtener datos de la API: {response.status_code}")
    
    todo = response.json()
    print(f"Datos del TODO obtenidos: {todo}")
    return todo

# Tarea para procesar el TODO
@task
def process_todo_data(todo):
    print(f"Procesando TODO con ID {todo['id']}: {todo['title']}")
    return {"id": todo['id'], "title": todo['title'], "completed": todo['completed']}

# Tarea para generar un reporte del TODO
@task
def generate_todo_report(processed_todo):
    status = "completada" if processed_todo['completed'] else "pendiente"
    print(f"Generando reporte para el TODO '{processed_todo['title']}' (ID: {processed_todo['id']}), Estado: {status}")

# Definición del flujo usando la nueva API de Prefect
@flow
async def todo_pipeline():
    # Obtener los datos del TODO desde la API
    todo = await fetch_todo_from_api()

    # Procesar los datos del TODO
    processed_todo = process_todo_data(todo)

    # Generar un reporte con los datos procesados
    generate_todo_report(processed_todo)

# Ejecuta el flujo
if __name__ == "__main__":
    asyncio.run(todo_pipeline())  # Ejecuta el flujo usando asyncio
