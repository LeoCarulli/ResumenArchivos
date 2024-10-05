import pdfplumber
import subprocess

# Definimos la ruta del archivo PDF
ruta_archivo = 'data/gatoconbotas.pdf'

# Abrimos el PDF y extraemos el texto
with pdfplumber.open(ruta_archivo) as pdf:
    texto_pdf = ""
    for pagina in pdf.pages:
        texto_pdf += pagina.extract_text()

# Preparamos el mensaje y ejecutamos el comando para generar el resumen
mensaje = f"Por favor, haceme un resumen detallado en español del siguiente texto:\n\n{texto_pdf}"
resumen = subprocess.run(['ollama', 'run', 'phi3.5'], input=mensaje, text=True, capture_output=True, encoding='utf-8').stdout

# Mostramos el resumen
print(resumen)
