import streamlit as st
import pandas as pd
import plotly.express as px

#Criação do Titulo
st.title("Relatório de Funcionário")

#Carregamento dos Dados
df = pd.read_csv("novos_dados.csv")
st.subheader("Tabela de Dados")
st.dataframe(df)

#Criação de Filtros
curso = st.selectbox("Selecione o departamento",df["departamento"].unique())
df_filtado = df[df["departamento"] == curso]
st.write(df_filtado)

#Elaboração de Grafico

barra = px.bar(
        df_filtado,
        x="nome_completo",
        y="salario_mensal_brl",
        color="nome_completo",
        title="Salário dos Funcionários"


)

st.plotly_chart(barra)