import os
import google.generativeai as genai
import telebot
from dotenv import load_dotenv # Nueva importación

# Esto carga las variables del archivo .env que está en la misma carpeta
load_dotenv() 

TOKEN = os.environ.get('TELEGRAM_TOKEN')
GEMINI_KEY = os.environ.get('GEMINI_API_KEY')

print(f"--- Iniciando Test KAIROS ---")
print(f"Token de Telegram detectado: {TOKEN[:5]}...") # Para ver si cargó algo

# Probar Gemini
try:
    genai.configure(api_key=GEMINI_KEY)
    
    # Usamos el nombre completo del modelo. 
    # Flash es mejor para estos tests por su velocidad.
    model = genai.GenerativeModel(model_name='gemini-2.5-flash')
    
    # Agregamos un mensaje simple
    response = model.generate_content("Hola Gemini, soy Alma. ¿Me escuchas?")
    
    if response.text:
        print(f"✅ Gemini responde: {response.text[:50]}...")
except Exception as e:
    print(f"❌ Error en Gemini: {e}")

# Probar Telegram
try:
    bot = telebot.TeleBot(TOKEN)
    me = bot.get_me()
    print(f"✅ Telegram conectado: @{me.username}")
except Exception as e:
    print(f"❌ Error en Telegram: {e}")