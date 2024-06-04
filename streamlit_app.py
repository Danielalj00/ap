import streamlit as st
import deepl
import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Configurar la API key de DeepL desde la variable de entorno
deepl_api_key = os.getenv('DEEPL_API_KEY')
translator = deepl.Translator(deepl_api_key)

st.title('Traducción Automática Multilingüe')

# Diccionario de modelos para traducción
model_dict = {
    "Español a Inglés": ("ES", "EN-US"),
    "Inglés a Español": ("EN", "ES"),
    "Francés a Inglés": ("FR", "EN-US"),
    "Inglés a Francés": ("EN", "FR"),
    "Alemán a Inglés": ("DE", "EN-US"),
    "Inglés a Alemán": ("EN", "DE"),
}

st.header('Seleccione el idioma de origen y destino')
option = st.selectbox('Selecciona la dirección de traducción', list(model_dict.keys()))

# Obtener los códigos de idioma
src_lang, dest_lang = model_dict[option]

# Entrada de texto del usuario
user_input = st.text_area(f'Texto a traducir ({src_lang} a {dest_lang})')

if st.button('Traducir'):
    if user_input:
        # Realizar la traducción
        result = translator.translate_text(user_input, source_lang=src_lang, target_lang=dest_lang)
        translated_text = result.text

        # Mostrar el texto traducido
        st.write('**Texto Traducido:**')
        st.write(translated_text)
    else:
        st.write("Por favor, ingrese un texto para traducir.")
