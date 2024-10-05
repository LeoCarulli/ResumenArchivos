# Resumen de Archivos

Este repo está pensado para automatizar la creación de resúmenes de archivos **PDF**, **Word** y **TXT** usando **Python**. La idea es que sea bien sencillo de entender, incluso si recién estás arrancando. Hay un **Jupyter Notebook** que explica paso a paso el proceso de generar un resumen de un PDF (para los que quieren entender el detalle), y después tenés los scripts en Python para usar en producción.

## Contenido

- **PDFpasoapaso.ipynb**: Un notebook donde te muestro paso a paso cómo hacer un resumen de un PDF. Este archivo está pensado para que puedas entender bien cómo funciona el proceso, pero no es lo ideal para usar.
- **PDFunificado.py**: Un script que genera resúmenes de archivos PDF de forma rápida. Es más general y está listo para usarlo en proyectos reales.
- **completo.py**: Es una mejora del anterior. Un script que te permite generar resúmenes de archivos de distintos formatos: PDF, Word y TXT. Solo admite la lectura de un archivo a la vez.
- **file_reader.py**: Contiene las funciones necesarias para leer archivos PDF, Word y TXT. Es usado solo por `completo.py` para facilitar la lectura de diferentes formatos.
- **requirements.txt**: Acá están todas las librerías que necesitás para que todo funcione sin problemas.
- **data/**: Es la carpeta donde tenés que poner el archivo que quieras resumir.

## Requisitos

Antes de correr los scripts, es recomendable que crees un entorno virtual para aislar las dependencias. Acá te dejo los pasos:

1. **Creá un entorno virtual** con el siguiente comando:

    ```bash
    python -m venv "nombre_del_entorno"
    ```

2. **Activá el entorno virtual**:
    - En Windows:
      ```bash
      nombre_del_entorno\Scripts\activate
      ```
    - En macOS/Linux:
      ```bash
      source nombre_del_entorno/bin/activate
      ```

3. **Instalá las librerías** que están en `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

## Cómo usar cada archivo

- **PDFpasoapaso.ipynb (Paso a paso con Jupyter Notebook)**
    - Abrí el archivo en Jupyter Notebook.
    - Seguí los pasos para ver cómo se genera el resumen de un PDF.
    - Este notebook es para entender el proceso, pero no es para uso en producción.

- **PDFunificado.py (Resúmenes para PDF)**
    - Si querés resumir un PDF rápidamente, usá este comando en la terminal:
      ```bash
      python PDFunificado.py
      ```
    - Asegurate de que el archivo PDF que querés resumir esté en la carpeta `data/`.

- **completo.py (Resúmenes para PDF, Word y TXT)**
    - Para resumir un archivo en cualquier formato (PDF, Word o TXT), ejecutá el siguiente comando:
      ```bash
      python completo.py
      ```
    - Solo podés trabajar con un archivo a la vez, así que asegurate de colocar el archivo correcto en la carpeta `data/`.

## Estructura del Proyecto

```bash
├── PDFpasoapaso.ipynb      # Paso a paso en Jupyter Notebook
├── PDFunificado.py         # Script para resumir PDF
├── completo.py             # Script para resumir un archivo (PDF, Word y TXT)
├── file_reader.py          # Funciones para leer los distintos tipos de archivos
├── requirements.txt        # Librerías necesarias
└── data/                   # Carpeta donde guardar el archivo a resumir
```
