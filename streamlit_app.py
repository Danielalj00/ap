import streamlit as st
from googletrans import Translator

st.title('Traducción Automática Multilingüe')

# Crear el traductor
translator = Translator()

# Diccionario de modelos para traducción
model_dict = {
    "Español a Inglés": ("es", "en"),
    "Inglés a Español": ("en", "es"),
    "Francés a Inglés": ("fr", "en"),
    "Inglés a Francés": ("en", "fr"),
    "Alemán a Inglés": ("de", "en"),
    "Inglés a Alemán": ("en", "de"),
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
        translated = translator.translate(user_input, src=src_lang, dest=dest_lang)
        translated_text = translated.text

        # Mostrar el texto traducido
        st.write('**Texto Traducido:**')
        st.write(translated_text)
    else:
        st.write("Por favor, ingrese un texto para traducir.")
