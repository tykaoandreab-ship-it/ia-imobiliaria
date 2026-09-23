import streamlit as st
import pandas as pd
import pickle

st.title("Avaliação Imobiliária com IA")

# Carregar o modelo treinado usando pickle nativo
try:
    with open('modelo_casas.pkl', 'rb') as f:
        model = pickle.load(f)
    st.success("Modelo carregado com sucesso!")
except Exception as e:
    st.error(f"Erro ao carregar o modelo: {e}")

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
    try:
        dados = [[med_inc, house_age, ave_rooms, ave_bedrms, population, ave_occup, latitude, longitude]]
        predicao = model.predict(dados)
        st.subheader(f"Valor Estimado: ${predicao[0] * 100000:.2f}")
    except Exception as e:
        st.error(f"Erro ao realizar a previsão: {e}")
