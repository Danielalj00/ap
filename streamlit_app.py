import streamlit as st
from transformers import MarianMTModel, MarianTokenizer

# Diccionario de modelos para traducción
model_dict = {
    "Español a Inglés": "Helsinki-NLP/opus-mt-es-en",
    "Inglés a Español": "Helsinki-NLP/opus-mt-en-es",
    "Francés a Inglés": "Helsinki-NLP/opus-mt-fr-en",
    "Inglés a Francés": "Helsinki-NLP/opus-mt-en-fr",
    "Alemán a Inglés": "Helsinki-NLP/opus-mt-de-en",
    "Inglés a Alemán": "Helsinki-NLP/opus-mt-en-de",
}

st.title('Traducción Automática Multilingüe')
st.header('Seleccione el idioma de origen y destino')

# Selección de idioma
option = st.selectbox('Selecciona la dirección de traducción', list(model_dict.keys()))

# Cargar el modelo y tokenizer seleccionados
model_name = model_dict[option]
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

# Entrada de texto del usuario
user_input = st.text_area(f'Texto a traducir ({option.split()[0]})')

if st.button('Traducir'):
    if user_input:
        # Tokenizar y traducir el texto
        inputs = tokenizer.encode(user_input, return_tensors="pt", max_length=512, truncation=True)
        translated_ids = model.generate(inputs, max_length=512, num_beams=4, early_stopping=True)
        translated_text = tokenizer.decode(translated_ids[0], skip_special_tokens=True)
        
        # Mostrar el texto traducido
        st.write('**Texto Traducido:**')
        st.write(translated_text)
    else:
        st.write("Por favor, ingrese un texto para traducir.")
