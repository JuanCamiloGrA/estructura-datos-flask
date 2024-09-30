# Estructuras de Datos con Flask

Este proyecto es una aplicación web desarrollada con Flask que permite gestionar dos estructuras de datos: Pilas y Colas. La aplicación permite crear, agregar, eliminar, modificar y mostrar elementos en estas estructuras.

## Características

- **Crear Estructura**: Permite crear una Pila o una Cola.
- **Agregar Elemento**: Permite agregar elementos a la Pila o Cola.
- **Eliminar Elemento**: Permite eliminar elementos de la Pila o Cola.
- **Modificar Estructura**: Permite modificar los elementos de la Pila o Cola.
- **Mostrar Estructura**: Permite visualizar los elementos actuales en la Pila o Cola.

## Requisitos

- Python 3.x
- pip (gestor de paquetes de Python)

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/JuanCamiloGrA/estructura-datos-flask.git
    cd estructura-datos-flask
    ```

2. Crea un entorno virtual:
    ```bash
    python -m venv .venv
    ```

3. Activa el entorno virtual:
    - En Windows:
        ```bash
        .venv\Scripts\activate
        ```
    - En macOS/Linux:
        ```bash
        source .venv/bin/activate
        ```

4. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Ejecuta la aplicación:
    ```bash
    python app.py
    ```

2. Abre tu navegador y ve a `http://127.0.0.1:5000`.

3. Utiliza la interfaz web para interactuar con las estructuras de datos.

## Estructura del Proyecto

- `app.py`: Archivo principal de la aplicación Flask.
- `base.py`: Archivo que contiene la clase base para las estructuras de datos.
- `pila.py`: Implementación de la clase Pila.
- `cola.py`: Implementación de la clase Cola.
- `templates/`: Directorio que contiene las plantillas HTML.
- `static/`: Directorio que contiene archivos estáticos (CSS en este caso).
- `.gitignore`: Archivo para ignorar archivos y directorios específicos en Git.

## Integrantes del Proyecto

- Juan Camilo Grisales Arias
- Juan Felipe Tarazona
- Kevin Andrés Betancourt López
