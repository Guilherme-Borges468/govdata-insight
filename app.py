import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="GovData Insight",
    page_icon="📊",
    layout="wide"
)

st.title("📊 GovData Insight")
st.subheader("Plataforma de análise de receitas e despesas municipais")

# ---------------------------
# DADOS FAKE PARA DEMONSTRAÇÃO
# ---------------------------

cidades = ["Buritirama", "Salvador", "Barreiras", "Feira de Santana", "Juazeiro"]

data = {
    "Cidade": np.random.choice(cidades, 200),
    "Receita": np.random.randint(100000, 1000000, 200),
    "Despesa": np.random.randint(50000, 900000, 200),
}

df = pd.DataFrame(data)

# KPIs
total_receita = df["Receita"].sum()
total_despesa = df["Despesa"].sum()
saldo = total_receita - total_despesa

col1, col2, col3 = st.columns(3)

col1.metric("💰 Receita Total", f"R$ {total_receita:,.0f}")
col2.metric("📉 Despesa Total", f"R$ {total_despesa:,.0f}")
col3.metric("📊 Saldo", f"R$ {saldo:,.0f}")

st.divider()

# ---------------------------
# FILTRO
# ---------------------------

cidade = st.selectbox("Selecione a cidade", ["Todas"] + cidades)

if cidade != "Todas":
    df = df[df["Cidade"] == cidade]

# ---------------------------
# GRÁFICOS
# ---------------------------

col1, col2 = st.columns(2)

with col1:
    st.subheader("Receitas por Cidade")
    receita_cidade = df.groupby("Cidade")["Receita"].sum()
    st.bar_chart(receita_cidade)

with col2:
    st.subheader("Despesas por Cidade")
    despesa_cidade = df.groupby("Cidade")["Despesa"].sum()
    st.bar_chart(despesa_cidade)

st.divider()

# ---------------------------
# TABELA
# ---------------------------

st.subheader("Dados detalhados")

st.dataframe(df, use_container_width=True)

st.divider()

st.info(
"""
Este dashboard é um protótipo da plataforma **GovData Insight**.

Objetivo do sistema:
- Centralizar dados de receitas e despesas municipais
- Automatizar coleta de dados públicos
- Permitir classificação e análise financeira
- Gerar relatórios estratégicos para tomada de decisão
"""
)