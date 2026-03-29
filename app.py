import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="GovData Insight",
    page_icon="📊",
    layout="wide"
)

st.title("📊 GovData Insight")
st.write("Sistema de demonstração para análise de dados financeiros municipais")

df = pd.read_csv("dados.csv")

receita_total = df["receita"].sum()
despesa_total = df["despesa"].sum()

col1, col2 = st.columns(2)

with col1:
    st.metric("Receita Total", f"R$ {receita_total:,.0f}")

with col2:
    st.metric("Despesa Total", f"R$ {despesa_total:,.0f}")

st.divider()

cidade = st.selectbox("Selecione uma cidade", df["cidade"])

cidade_df = df[df["cidade"] == cidade]

st.subheader("Dados da cidade selecionada")
st.dataframe(cidade_df, use_container_width=True)

st.subheader("Comparação entre cidades")

chart_data = df.set_index("cidade")[["receita", "despesa"]]

st.bar_chart(chart_data)

st.subheader("Tabela completa")

st.dataframe(df, use_container_width=True)