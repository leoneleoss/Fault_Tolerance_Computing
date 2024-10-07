
# Proyecto: Flujo de Trabajo con Prefect y API de JSONPlaceholder

Este proyecto es un ejemplo de cómo usar Prefect para gestionar tareas asíncronas y realizar operaciones con una API de REST (JSONPlaceholder). En este flujo, se obtienen datos de múltiples tareas (`todos`), se filtran los completados y se genera un reporte de estos.

## Descripción

El proyecto consiste en un flujo que realiza lo siguiente:

1. Obtiene una lista de tareas (todos) desde la API de JSONPlaceholder (`https://jsonplaceholder.cypress.io/todos`).
2. Filtra las tareas que han sido completadas.
3. Genera un reporte en la consola mostrando los `todos` que están completados.

## Estructura del Proyecto

- `main.py`: Archivo principal que contiene el código del flujo.
- `README.md`: Este archivo, que explica el funcionamiento del proyecto.

## Requisitos

- Python 3.8+
- [Prefect](https://docs.prefect.io/getting-started/installation/) (Versión moderna compatible con Prefect 2.x)
- [httpx](https://www.python-httpx.org/) para hacer las solicitudes HTTP de manera asíncrona.

### Instalación de dependencias

Puedes instalar las dependencias necesarias con los siguientes comandos:

```bash
pip install prefect httpx
```

## Estructura del Código

### `fetch_todos_from_api()`

Esta tarea obtiene una lista de todos los `todos` desde la API de JSONPlaceholder. Si hay un error en la solicitud, se intenta de nuevo hasta 3 veces con un retraso de 10 segundos entre cada intento.

### `filter_completed_todos()`

Esta tarea toma la lista de `todos` y filtra aquellos que han sido completados (`completed: true`).

### `generate_completed_todos_report()`

Esta tarea genera un reporte simple de los `todos` completados, mostrando su título e ID.

## Ejecución del Flujo

El flujo se puede ejecutar llamando al script `main.py`:

```bash
python main.py
```

Esto hará lo siguiente:

1. Realiza una solicitud a la API para obtener los `todos`.
2. Filtra los `todos` que están completados.
3. Muestra un reporte en la consola de las tareas completadas.

### Ejemplo de salida:

```bash
Datos de los TODOs obtenidos: [{'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': false}, ...]
Se encontraron 90 TODOs completados.
Generando reporte de TODOs completados:
- TODO 'quis ut nam facilis et officia qui' (ID: 4) está completado.
- TODO 'fugiat veniam minus' (ID: 6) está completado.
...
```

## Modificaciones Realizadas

Se tomó un flujo básico de Prefect y se modificó para:

- Obtener múltiples datos de una API externa.
- Agregar una funcionalidad de filtro para los `todos` completados.
- Generar un reporte sencillo de esos datos filtrados.

## Enlaces

- **JSONPlaceholder API**: [https://jsonplaceholder.cypress.io](https://jsonplaceholder.cypress.io)
- **Prefect**: [https://www.prefect.io](https://www.prefect.io)
