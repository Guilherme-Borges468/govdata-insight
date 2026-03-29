import streamlit as st
import pandas as pd

st.set_page_config(page_title="GovData Insight", layout="wide")

st.title("📊 GovData Insight")
st.subheader("Sistema de análise de dados financeiros municipais")

df = pd.read_csv("dados.csv")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Receita Total",
        f"R$ {df['receita'].sum():,.0f}"
    )

with col2:
    st.metric(
        "Despesa Total",
        f"R$ {df['despesa'].sum():,.0f}"
    )

st.divider()

cidade = st.selectbox(
    "Selecionar cidade",
    df["cidade"]
)

cidade_df = df[df["cidade"] == cidade]

st.write("### Dados da cidade")

st.dataframe(cidade_df)

st.write("### Comparação entre cidades")

st.bar_chart(
    df.set_index("cidade")[["receita", "despesa"]]
)

st.write("### Dados completos")

st.dataframe(df)