# Resumen de Archivos
Este repo está pensado para automatizar la creación de resúmenes de archivos **PDF** usando **Python**. La idea es que sea bien sencillo de entender, incluso si recién estás arrancando. Hay un **Jupyter Notebook** que explica paso a paso el proceso de generar un resumen de un PDF (para los que quieren entender el detalle), y después tenés el script en Python para usar en producción.

## Contenido

- **PDFpasoapaso.ipynb**: Un notebook donde te muestro paso a paso cómo hacer un resumen de un PDF. Este archivo está pensado para que puedas entender bien cómo funciona el proceso, pero no es lo ideal para usar.
- **PDFunificado.py**: Un script que genera resúmenes de archivos PDF de forma rápida. Es más general y está listo para usarlo en proyectos reales.
- **requirements.txt**: Acá están todas las librerías que necesitás para que todo funcione sin problemas.
- **data/**: Es la carpeta donde tenés que poner el archivo que quieras resumir.

## Requisitos


1. **Instalá Python** desde [este enlace](https://www.python.org/downloads/).

2. **Instalá Visual Studio Code** desde [este enlace](https://code.visualstudio.com/download) o cualquier editor de código de tu preferencia. Recomiendo Visual Studio Code por su facilidad de uso y funcionalidades.

Para el archivo **PDFpasoapaso.ipynb**, con esto ya debería ser suficiente para poder correrlo.

3. **Creá un entorno virtual** con el siguiente comando:

  ```bash
  python -m venv "nombre_del_entorno"
  ```

4. **Activá el entorno virtual**:
  - En Windows:
    ```bash
    nombre_del_entorno\Scripts\activate
    ```
  - En macOS/Linux:
    ```bash
    source nombre_del_entorno/bin/activate
    ```

5. **Instalá las librerías** que están en `requirements.txt`:
  ```bash
  pip install -r requirements.txt
  ```



## Cómo usar cada archivo

- **PDFpasoapaso.ipynb (Paso a paso con Jupyter Notebook)**
  - Abrí el archivo en Jupyter Notebook.
  - Seguí los pasos para ver cómo se genera el resumen de un PDF.
  - Este notebook es para entender el proceso, pero no es ideal para uso en producción.

- **PDFunificado.py (Resúmenes para PDF)**
  - Si querés resumir un PDF rápidamente, usá este comando en la terminal:
    ```bash
    python PDFunificado.py
    ```
  - Asegurate de que el archivo PDF que querés resumir esté en la carpeta `data/`.

## Estructura del Proyecto

```bash
├── PDFpasoapaso.ipynb      # Paso a paso en Jupyter Notebook
├── PDFunificado.py         # Script para resumir PDF
├── requirements.txt        # Librerías necesarias
└── data/                   # Carpeta donde guardar el archivo a resumir
```
