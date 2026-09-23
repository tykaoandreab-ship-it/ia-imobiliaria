
import streamlit as st
import pandas as pd

st.title("Avaliação Imobiliária com IA")

st.success("Aplicação carregada com sucesso!")

# Formulário de entrada de dados
med_inc = st.number_input("Renda Média da Região (MedInc)", value=3.5)
house_age = st.number_input("Idade Média do Imóvel (HouseAge)", value=15.0)
ave_rooms = st.number_input("Número Médio de Cómodos (AveRooms)", value=5.0)
ave_bedrms = st.number_input("Número Médio de Quartos (AveBedrms)", value=1.0)
population = st.number_input("População da Região", value=1000.0)
ave_occup = st.number_input("Média de Ocupantes", value=3.0)
latitude = st.number_input("Latitude", value=37.88)
longitude = st.number_input("Longitude", value=-122.23)

if st.button("Calcular Preço Estimado"):
    # Modelo estimativo baseado nos parâmetros
    preco_base = (med_inc * 40000) + (ave_rooms * 15000) - (house_age * 500) - (ave_occup * 2000)
    if preco_base < 30000:
        preco_base = 30000
    st.subheader(f"Valor Estimado: ${preco_base:,.2f}")
    
