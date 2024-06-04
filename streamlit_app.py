import streamlit as st
import openai
import os

# Configurar la API key de OpenAI desde la variable de entorno
openai.api_key = os.getenv('OPENAI_API_KEY')

st.title('Generación de Texto Creativo en Español')
st.header('Ingrese un tema o idea para generar texto creativo')

# Entrada de texto del usuario
user_input = st.text_input('Tema o idea:')

# Selección del tipo de texto creativo
text_type = st.selectbox(
    'Seleccione el tipo de texto que desea generar',
    ('Historia', 'Poema', 'Artículo')
)

if st.button('Generar Texto'):
    if user_input:
        # Crear el prompt basado en el tipo de texto seleccionado
        prompt = f"Escribe un(a) {text_type.lower()} sobre {user_input} en español"
        
        # Realizar la consulta al modelo de OpenAI
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7
        )
        st.write(f'**{text_type} Generado:**')
        st.write(response.choices[0].text.strip())
    else:
        st.write("Por favor, ingrese un tema o idea para generar texto creativo.")


