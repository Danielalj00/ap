import streamlit as st
from translate import Translator

st.title('Traducción Automática Multilingüe')

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

# Crear el traductor
translator = Translator(from_lang=src_lang, to_lang=dest_lang)

# Entrada de texto del usuario
user_input = st.text_area(f'Texto a traducir ({src_lang} a {dest_lang})')

if st.button('Traducir'):
    if user_input:
        # Realizar la traducción
        translated_text = translator.translate(user_input)

        # Mostrar el texto traducido
        st.write('**Texto Traducido:**')
        st.write(translated_text)
    else:
        st.write("Por favor, ingrese un texto para traducir.")
