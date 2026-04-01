import streamlit as st
import pandas as pd
import plotly.express as px

#Criação do Titulo
st.title("Relatório de Cadastro Escolar")

#Carregamento dos Dados
df = pd.read_csv("base_alunos_10_prova.csv")
st.subheader("Tabela de Dados dos Alunos")
st.dataframe(df)

#Criação de Filtros
curso = st.selectbox("Selecione a situação do Aluno",df["curso_aluno"].unique())
df_filtado = df[df["curso_aluno"] == curso]
st.write(df_filtado)

#Elaboração de Grafico

barra = px.bar(
        df_filtado,
        x="curso_aluno",
        y="situacao",
        color="curso_aluno",
        title="Cursos x Idade"


)

st.plotly_chart(barra)