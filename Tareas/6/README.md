
# Proyecto: Flujo de Trabajo con Prefect y API de JSONPlaceholder

Este proyecto es un ejemplo de cómo usar Prefect para gestionar tareas asíncronas y realizar operaciones con una API de REST (JSONPlaceholder). En este flujo, se obtienen datos de múltiples tareas (`todos`), se filtran los completados y se genera un reporte de estos.

## Descripción

El proyecto consiste en un flujo que realiza las siguientes tareas:

1. **Obtención de Datos**: Hace una solicitud a la API de [JSONPlaceholder](https://jsonplaceholder.cypress.io/todos) para obtener una lista de TODOs.
2. **Filtrado de TODOs Completados**: Filtra los TODOs para conservar solo aquellos que están completados.
3. **Almacenamiento en Base de Datos**: Almacena los TODOs completados en una base de datos SQLite.
4. **Generación de Reporte**: Genera un reporte en la consola con los detalles de los TODOs completados.

## Estructura del Proyecto

- `main.py`: Archivo principal que contiene el código del flujo.
- `todos.db`: Archivo que contiene los datos guardados de la api

## Requisitos

- Python 3.8+
- [Prefect](https://docs.prefect.io/getting-started/installation/) (Versión moderna compatible con Prefect 2.x)
- [httpx](https://www.python-httpx.org/) para hacer las solicitudes HTTP de manera asíncrona.
- SQLite (incluido en Python)

### Instalación de dependencias

```bash
pip install prefect
```

```bash
pip install httpx
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
3. Revisa los datos almacenados en la base de datos `todos.db`. Puedes abrirla usando cualquier herramienta que soporte SQLite.
3. Muestra un reporte en la consola de las tareas completadas.

### Ejemplo de salida:

```bash
11:15:16.570 | INFO    | prefect - Starting server on http://127.0.0.1:8196
11:15:20.943 | INFO    | prefect.engine - Created flow run 'colossal-rattlesnake' for flow 'todo-pipeline'
11:15:21.299 | INFO    | Task run 'fetch_todos_from_api-b82' - Created task run 'fetch_todos_from_api-b82' for task 'fetch_todos_from_api'


Datos del TODO 1:
{'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
Datos del TODO 2:
{'userId': 1, 'id': 2, 'title': 'quis ut nam facilis et officia qui', 'completed': False}   
Datos del TODO 3:
{'userId': 1, 'id': 3, 'title': 'fugiat veniam minus', 'completed': False}

  . . . 

11:15:22.154 | INFO    | Task run 'fetch_todos_from_api-b82' - Finished in state Completed()
11:15:22.420 | INFO    | Task run 'filter_completed_todos-c8a' - Created task run 'filter_completed_todos-c8a' for task 'filter_completed_todos'


Se encontraron 90 TODOs completados.


11:15:22.429 | INFO    | Task run 'filter_completed_todos-c8a' - Finished in state Completed()
11:15:22.680 | INFO    | Task run 'store_completed_todos_in_db-991' - Created task run 'store_completed_todos_in_db-991' for task 'store_completed_todos_in_db'

Cargadas 90 tareas completadas en la base de datos.

11:15:22.689 | INFO    | Task run 'store_completed_todos_in_db-991' - Finished in state Completed()
11:15:22.942 | INFO    | Task run 'generate_completed_todos_report-ef6' - Created task run 'generate_completed_todos_report-ef6' for task 'generate_completed_todos_report'


Generando reporte de TODOs completados:
- TODO 'et porro tempora' (ID: 4) está completado.
- TODO 'quo adipisci enim quam ut ab' (ID: 8) está completado.
- TODO 'illo est ratione doloremque quia maiores aut' (ID: 10) está completado.
- TODO 'vero rerum temporibus dolor' (ID: 11) está completado.
- TODO 'ipsa repellendus fugit nisi' (ID: 12) está completado.
- TODO 'repellendus sunt dolores architecto voluptatum' (ID: 14) está completado.
- TODO 'ab voluptatum amet voluptas' (ID: 15) está completado.
- TODO 'accusamus eos facilis sint et aut voluptatem' (ID: 16) está completado.
- TODO 'quo laboriosam deleniti aut qui' (ID: 17) está completado.
- TODO 'molestiae ipsa aut voluptatibus pariatur dolor nihil' (ID: 19) está completado.
- TODO 'ullam nobis libero sapiente ad optio sint' (ID: 20) está completado.
- TODO 'distinctio vitae autem nihil ut molestias quo' (ID: 22) está completado.
- TODO 'voluptas quo tenetur perspiciatis explicabo natus' (ID: 25) está completado.
- TODO 'aliquam aut quasi' (ID: 26) está completado.
- TODO 'veritatis pariatur delectus' (ID: 27) está completado.
- TODO 'nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis' (ID: 30) está completado.
- TODO 'repellendus veritatis molestias dicta incidunt' (ID: 35) está completado.
- TODO 'excepturi deleniti adipisci voluptatem et neque optio illum ad' (ID: 36) está completado.
- TODO 'totam atque quo nesciunt' (ID: 40) está completado.
- TODO 'tempore ut sint quis recusandae' (ID: 43) está completado.
- TODO 'cum debitis quis accusamus doloremque ipsa natus sapiente omnis' (ID: 44) está completado.
- TODO 'cupiditate necessitatibus ullam aut quis dolor voluptate' (ID: 50) está completado.
- TODO 'quis et est ut voluptate quam dolor' (ID: 54) está completado.
- TODO 'voluptatum omnis minima qui occaecati provident nulla voluptatem ratione' (ID: 55) está completado.
- TODO 'deleniti ea temporibus enim' (ID: 56) está completado.
- TODO 'et sequi qui architecto ut adipisci' (ID: 60) está completado.
- TODO 'odit optio omnis qui sunt' (ID: 61) está completado.
- TODO 'doloremque aut dolores quidem fuga qui nulla' (ID: 63) está completado.
- TODO 'sint amet quia totam corporis qui exercitationem commodi' (ID: 73) está completado.
- TODO 'sequi dolorem sed' (ID: 76) está completado.
- TODO 'eum ipsa maxime ut' (ID: 79) está completado.
- TODO 'tempore molestias dolores rerum sequi voluptates ipsum consequatur' (ID: 80) está completado.
- TODO 'suscipit qui totam' (ID: 81) está completado.
- TODO 'quidem at rerum quis ex aut sit quam' (ID: 83) está completado.
- TODO 'et quia ad iste a' (ID: 85) está completado.
- TODO 'incidunt ut saepe autem' (ID: 86) está completado.
- TODO 'laudantium quae eligendi consequatur quia et vero autem' (ID: 87) está completado.
- TODO 'sequi ut omnis et' (ID: 89) está completado.
- TODO 'molestiae nisi accusantium tenetur dolorem et' (ID: 90) está completado.
- TODO 'nulla quis consequatur saepe qui id expedita' (ID: 91) está completado.
- TODO 'in omnis laboriosam' (ID: 92) está completado.
- TODO 'odio iure consequatur molestiae quibusdam necessitatibus quia sint' (ID: 93) está completado.
- TODO 'vel nihil et molestiae iusto assumenda nemo quo ut' (ID: 95) está completado.
- TODO 'debitis accusantium ut quo facilis nihil quis sapiente necessitatibus' (ID: 98) está completado.
- TODO 'totam quia dolorem et illum repellat voluptas optio' (ID: 105) está completado.
- TODO 'ad illo quis voluptatem temporibus' (ID: 106) está completado.
- TODO 'a eos eaque nihil et exercitationem incidunt delectus' (ID: 108) está completado.
- TODO 'autem temporibus harum quisquam in culpa' (ID: 109) está completado.
- TODO 'aut aut ea corporis' (ID: 110) está completado.
- TODO 'ipsa dolores vel facilis ut' (ID: 116) está completado.
- TODO 'inventore aut nihil minima laudantium hic qui omnis' (ID: 121) está completado.
- TODO 'provident aut nobis culpa' (ID: 122) está completado.
- TODO 'ut asperiores perspiciatis veniam ipsum rerum saepe' (ID: 126) está completado.
- TODO 'voluptatem libero consectetur rerum ut' (ID: 127) está completado.
- TODO 'nulla aliquid eveniet harum laborum libero alias ut unde' (ID: 130) está completado.
- TODO 'qui molestiae voluptatibus velit iure harum quisquam' (ID: 132) está completado.
- TODO 'et labore eos enim rerum consequatur sunt' (ID: 133) está completado.
- TODO 'placeat minima consequatur rem qui ut' (ID: 138) está completado.
- TODO 'aut consectetur in blanditiis deserunt quia sed laboriosam' (ID: 140) está completado.
- TODO 'explicabo consectetur debitis voluptates quas quae culpa rerum non' (ID: 141) está completado.
- TODO 'maiores accusantium architecto necessitatibus reiciendis ea aut' (ID: 142) está completado.
- TODO 'molestiae suscipit ratione nihil odio libero impedit vero totam' (ID: 146) está completado.
- TODO 'eum itaque quod reprehenderit et facilis dolor autem ut' (ID: 147) está completado.
- TODO 'accusamus adipisci dicta qui quo ea explicabo sed vero' (ID: 151) está completado.
- TODO 'rerum non ex sapiente' (ID: 154) está completado.
- TODO 'voluptatem nobis consequatur et assumenda magnam' (ID: 155) está completado.
- TODO 'nam quia quia nulla repellat assumenda quibusdam sit nobis' (ID: 156) está completado.
- TODO 'dolorem veniam quisquam deserunt repellendus' (ID: 157) está completado.
- TODO 'debitis vitae delectus et harum accusamus aut deleniti a' (ID: 158) está completado.
- TODO 'debitis adipisci quibusdam aliquam sed dolore ea praesentium nobis' (ID: 159) está completado.
- TODO 'ex hic consequuntur earum omnis alias ut occaecati culpa' (ID: 161) está completado.
- TODO 'omnis laboriosam molestias animi sunt dolore' (ID: 162) está completado.
- TODO 'ea odio perferendis officiis' (ID: 169) está completado.
- TODO 'fugiat aut voluptatibus corrupti deleniti velit iste odio' (ID: 171) está completado.
- TODO 'laudantium eius officia perferendis provident perspiciatis asperiores' (ID: 175) está completado.
- TODO 'nesciunt itaque commodi tempore' (ID: 178) está completado.
- TODO 'omnis consequuntur cupiditate impedit itaque ipsam quo' (ID: 179) está completado.
- TODO 'debitis nisi et dolorem repellat et' (ID: 180) está completado.
- TODO 'inventore saepe cumque et aut illum enim' (ID: 182) está completado.
- TODO 'omnis nulla eum aliquam distinctio' (ID: 183) está completado.
- TODO 'vel non beatae est' (ID: 188) está completado.
- TODO 'culpa eius et voluptatem et' (ID: 189) está completado.
- TODO 'accusamus sint iusto et voluptatem exercitationem' (ID: 190) está completado.
- TODO 'temporibus atque distinctio omnis eius impedit tempore molestias pariatur' (ID: 191) está completado.
- TODO 'rerum debitis voluptatem qui eveniet tempora distinctio a' (ID: 193) está completado.
- TODO 'rerum ex veniam mollitia voluptatibus pariatur' (ID: 195) está completado.
- TODO 'consequuntur aut ut fugit similique' (ID: 196) está completado.
- TODO 'dignissimos quo nobis earum saepe' (ID: 197) está completado.
- TODO 'quis eius est sint explicabo' (ID: 198) está completado.
- TODO 'numquam repellendus a magnam' (ID: 199) está completado.
11:15:22.957 | INFO    | Task run 'generate_completed_todos_report-ef6' - Finished in state Completed()
11:15:23.016 | INFO    | Flow run 'colossal-rattlesnake' - Finished in state Completed()
11:15:23.040 | INFO    | prefect - Stopping server on http://127.0.0.1:8196
```

## Enlaces

- **JSONPlaceholder API**: [https://jsonplaceholder.cypress.io](https://jsonplaceholder.cypress.io)
- **Prefect**: [https://www.prefect.io](https://www.prefect.io)
- **Getting Started with Prefect (PyData Denver)**: [https://www.youtube.com/watch?v=FETN0iivZps](https://www.youtube.com/watch?v=FETN0iivZps)