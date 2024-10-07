# Resumen de Archivos
Este repo está pensado para automatizar la creación de resúmenes de archivos **PDF** usando **Python** y **Ollama**. Está pensado para ser fácil de entender, incluso para quienes recién empiezan.

Incluye un **Jupyter Notebook** que explica paso a paso el proceso de generar resúmenes, y un script en Python listo para producción.

## Contenido

- **PDFpasoapaso.ipynb**: Notebook que explica el proceso de resumen de un PDF paso a paso. Es ideal para entender cómo funciona, pero no para producción.
- **PDFunificado.py**: Script que genera resúmenes de PDF de forma rápida y general para proyectos reales.
- **requirements.txt**: Acá están todas las librerías que necesitás para que todo funcione sin problemas.
- **data/**: Es la carpeta donde tenés que poner el archivo que quieras resumir.

## Requisitos

1. **Instalá Python** desde [Python](https://www.python.org/downloads/).

2. **Instalá Visual Studio Code** desde [VSC](https://code.visualstudio.com/download) o cualquier editor de código de tu preferencia. Recomiendo Visual Studio Code por su facilidad de uso y funcionalidades.

3. **Descargá e instalá Ollama** desde [Ollama](https://ollama.com/) y el modelo de lenguaje natural que prefieras desde [Library](https://ollama.com/library).

En nuestro código, tenemos seteado por default el modelo **phi3.5**, el cual podes descargar aquí: [Phi3.5](https://ollama.com/library/phi3.5)

Requisitos para Ejecutar el Modelo phi3.5 de Ollama

- GPU (recomendada): NVIDIA GTX 1080 o superior, con al menos 4 GB de VRAM. 
- RAM: 16 GB o más para un rendimiento óptimo. Sin GPU, es posible que se necesite más memoria RAM para evitar problemas de rendimiento.

Nota sobre el uso sin GPU: El modelo puede ejecutarse solo con CPU, pero será más lento, especialmente para tareas complejas, y consumirá más RAM. Sin GPU, es mejor para tareas pequeñas o experimentación.

- Para el archivo **PDFpasoapaso.ipynb**, con esto ya debería ser suficiente para poder correrlo celda a celda.

- Para el archivo **PDFunificado.py**, también es necesario instalar las librerías correspondientes. En este caso, se puede hacer a través del siguiente comando desde la consola:

```bash
pip install pdfplumber
```
Sin embargo, es una buena práctica en este tipo de proyectos, crear un entorno virtual con todas las dependencias necesarias para evitar problemas de incompatibilidad entre versiones. Te dejo un ejemplo de cómo crear el entorno virtual, activarlo e instalar las dependencias necesarias:

1. **Creá un entorno virtual** con el siguiente comando:

  ```bash
  python -m venv "nombre_del_entorno"
  ```

2. **Activá el entorno virtual**:
  - En Windows:
    ```bash
    nombre_del_entorno\Scripts\activate
    ```
    > Puede que haya un error si es la primera vez que lo haces. Se soluciona ejecutando el siguiente comando:
    > ```bash
    > Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    > ```
  - En macOS/Linux:
    ```bash
    source nombre_del_entorno/bin/activate
    ```

3. **Instalá las librerías** que están en `requirements.txt`:
  ```bash
  pip install -r requirements.txt
  ```


 En este caso, en el archivo llamado `requirements.txt`, esas dependencias están presentes. (En este ejemplo, solo la librería "pdfplumber")


## Cómo usar cada archivo

- **PDFpasoapaso.ipynb (Paso a paso con Jupyter Notebook)**: Abrir en Jupyter Notebook y seguir las instrucciones paso a paso para entender el proceso.
- **PDFunificado.py (Resúmenes para PDF)**: Si querés resumir un PDF rápidamente, usá este comando en la terminal (siempre estando sobre la carpeta donde está el archivo a ejecutar):
    ```bash
    python PDFunificado.py
    ```
Asegurate de que el archivo PDF que querés resumir esté en la carpeta `data/`.

## Estructura del Proyecto

```bash
├── PDFpasoapaso.ipynb      # Paso a paso en Jupyter Notebook
├── PDFunificado.py         # Script para resumir PDF
├── requirements.txt        # Librerías necesarias
└── data/                   # Carpeta donde guardar el archivo a resumir
```
