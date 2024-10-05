import os  # Para manejar rutas de archivos
import PyPDF2  # Librería para leer PDFs
import subprocess  # Para ejecutar comandos del sistema

# Ruta del archivo PDF
ruta_archivo = os.path.join('data', 'gatoconbotas.pdf')

# Función que extrae el texto del PDF
def extraer_texto_pdf(ruta_pdf):
    # Chequeamos si el archivo existe
    if not os.path.exists(ruta_pdf):
        print(f"El archivo {ruta_pdf} no existe.")
        return None
    try:
        # Abrimos el PDF y leemos el contenido
        with open(ruta_pdf, 'rb') as archivo:
            lector_pdf = PyPDF2.PdfReader(archivo)
            texto = ''.join([pagina.extract_text() for pagina in lector_pdf.pages])
        return texto
    except Exception as e:
        print(f"Error al leer el PDF: {e}")
        return None

# Función para generar un resumen con Ollama
def generar_resumen(texto, modelo='llama3'):
    try:
        # Preparamos el mensaje para que Ollama genere un resumen en español latino
        mensaje = f"Por favor, haceme un resumen en español:\n\n{texto}"
        
        # Ejecutamos el modelo llamando a Ollama desde la terminal
        result = subprocess.run(['ollama', 'run', modelo], input=mensaje, text=True, capture_output=True, encoding='utf-8')
        
        # Si todo salió bien, mostramos el resumen
        if result.returncode == 0:
            return result.stdout
        else:
            print(f"Error al generar el resumen: {result.stderr}")
            return None
    except Exception as e:
        print(f"Error inesperado: {e}")
        return None

# Función principal
def main():
    # Extraemos el texto del PDF
    texto_pdf = extraer_texto_pdf(ruta_archivo)
    
    # Si hay texto, generamos el resumen
    if texto_pdf:
        resumen = generar_resumen(texto_pdf)
        if resumen:
            print("Resumen generado:")
            print(resumen)
        else:
            print("No se pudo generar el resumen.")
    else:
        print("No se pudo extraer texto del PDF.")

# Ejecutamos el script
if __name__ == "__main__":
    main()
