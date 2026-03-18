import os
import telebot
import google.generativeai as genai
from telebot import types
import PyPDF2

# 1. Configuración de APIs
TOKEN = os.environ.get('TELEGRAM_TOKEN')
GEMINI_KEY = os.environ.get('GEMINI_API_KEY')

genai.configure(api_key=GEMINI_KEY)

# --- DEFINICIÓN DE TOOLS ---
def escribir_archivo(nombre_archivo: str, contenido: str):
    """Crea o actualiza un archivo en el proyecto. Úsalo para código Kotlin (.kt), notas o docs (.md)."""
    # Mapeo de rutas según tu estructura de Docker
    if nombre_archivo.endswith('.kt'):
        ruta_base = "/app/raiz_proyecto/codigo_fuente"
    elif nombre_archivo.endswith('.md'):
        ruta_base = "/app/docs_tecnicos"
    else:
        ruta_base = "/app/raiz_proyecto"

    ruta_final = os.path.join(ruta_base, nombre_archivo)
    
    try:
        os.makedirs(os.path.dirname(ruta_final), exist_ok=True)
        with open(ruta_final, 'w', encoding='utf-8') as f:
            f.write(contenido)
        return f"✅ Archivo '{nombre_archivo}' creado exitosamente en {ruta_final}"
    except Exception as e:
        return f"❌ Error al crear el archivo: {str(e)}"

# Inicializamos el modelo con la capacidad de usar herramientas
model = genai.GenerativeModel(
    model_name='gemini-2.5-flash',
    tools=[escribir_archivo]
)

bot = telebot.TeleBot(TOKEN)

# 2. Función para leer contexto local (incluye Identity y Soul)
def obtener_contexto_local():
    contexto = ""
    rutas = ['/app/documentos', '/app/docs_tecnicos', '/app/contexto', '/app/raiz_proyecto']
    
    for ruta in rutas:
        if os.path.exists(ruta):
            for archivo in os.listdir(ruta):
                ruta_completa = os.path.join(ruta, archivo)
                
                # Leer Markdown (aquí entrarán identity.md y soul.md)
                if archivo.endswith((".txt", ".md")):
                    try:
                        with open(ruta_completa, 'r', encoding='utf-8') as f:
                            contexto += f"\n\n--- DOCUMENTO ({archivo}): ---\n{f.read()}\n"
                    except Exception as e:
                        print(f"Error leyendo {archivo}: {e}")
                
                # Leer PDFs
                elif archivo.endswith(".pdf"):
                    try:
                        with open(ruta_completa, 'rb') as f:
                            lector = PyPDF2.PdfReader(f)
                            texto_pdf = ""
                            for i in range(min(3, len(lector.pages))):
                                texto_pdf += lector.pages[i].extract_text()
                            contexto += f"\n\n--- PDF ({archivo}): ---\n{texto_pdf[:2000]}\n"
                    except Exception as e:
                        print(f"Error leyendo PDF {archivo}: {e}")
    return contexto

# 3. Manejador de mensajes con Function Calling automático
@bot.message_handler(func=lambda message: True)
def responder(message):
    contexto_archivos = obtener_contexto_local()
    
    # Iniciamos un chat que gestiona automáticamente las llamadas a funciones
    chat = model.start_chat(enable_automatic_function_calling=True)
    
    prompt_maestro = (
        f"INSTRUCCIONES DE IDENTIDAD Y CONTEXTO:\n{contexto_archivos}\n\n"
        f"Eres el Mentor de Tesis de Alma. Tu objetivo es ayudar con el MVP de KAIROS.\n"
        f"Si Alma te pide código o crear documentos, usa la herramienta 'escribir_archivo'.\n\n"
        f"Pregunta de Alma: {message.text}"
    )
    
    try:
        response = chat.send_message(prompt_maestro)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, f"❌ Error en el motor: {str(e)}")

print("🚀 KAIROS Agente Activo con Identity & Tools...")
bot.infinity_polling()