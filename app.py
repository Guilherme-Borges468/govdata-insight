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
# CARREGAR DADOS REAIS
# ---------------------------

try:
    df = pd.read_csv('dados.csv')
    df.columns = df.columns.str.title()  # cidade -> Cidade, receita -> Receita, etc.
    df['Receita'] = pd.to_numeric(df['Receita'], errors='coerce')
    df['Despesa'] = pd.to_numeric(df['Despesa'], errors='coerce')
    st.success(f"✅ Dados carregados com sucesso ({len(df)} registros)!")
except Exception as e:
    st.error(f"❌ Erro ao carregar dados.csv: {e}")
    st.stop()

# KPIs
total_receita = df["Receita"].sum()
total_despesa = df["Despesa"].sum()
saldo = total_receita - total_despesa if not pd.isna(total_receita) and not pd.isna(total_despesa) else 0

col1, col2, col3 = st.columns(3)

col1.metric("💰 Receita Total", f"R$ {total_receita:,.0f}")
col2.metric("📉 Despesa Total", f"R$ {total_despesa:,.0f}")
col3.metric("📊 Saldo", f"R$ {saldo:,.0f}")

st.divider()

# ---------------------------
# FILTRO
# ---------------------------

cidades = sorted(df["Cidade"].unique())
cidade = st.selectbox("Selecione a cidade", ["Todas"] + cidades)

if cidade != "Todas":
    df_filtered = df[df["Cidade"] == cidade].copy()
else:
    df_filtered = df.copy()

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

st.dataframe(df_filtered, width="stretch")

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
