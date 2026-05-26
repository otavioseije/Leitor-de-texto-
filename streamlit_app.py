import streamlit as st
import google.generativeai as genai
import os

# Configura a chave da API (o Streamlit buscará isso nas configurações de "Secrets")
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

st.title("Esotericus - Leitor Inteligente")

texto = st.text_area("Cole o texto do seu livro aqui:")

if st.button("Analisar Tradução Esotérica"):
    if texto:
        model = genai.GenerativeModel('gemini-pro')
        resposta = model.generate_content(f"Analise e traduza este texto com uma abordagem acadêmica e esotérica: {texto}")
        st.write(resposta.text)
    else:
        st.warning("Por favor, cole um texto primeiro.")
