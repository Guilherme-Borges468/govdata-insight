import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="GovData Insight",
    page_icon="📊",
    layout="wide"
)

# -----------------------
# LOGIN
# -----------------------

def login():

    st.title("🔐 GovData Insight")
    st.subheader("Sistema de Análise de Despesas Públicas")

    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):

        if usuario == "admin" and senha == "admin123":
            st.session_state["logado"] = True
            st.rerun()

        else:
            st.error("Usuário ou senha inválidos")


if "logado" not in st.session_state:
    st.session_state["logado"] = False


if not st.session_state["logado"]:
    login()
    st.stop()


# -----------------------
# SIDEBAR
# -----------------------

st.sidebar.title("GovData Insight")

pagina = st.sidebar.radio(
    "Navegação",
    ["Dashboard", "Despesas", "Relatórios"]
)

if st.sidebar.button("Sair"):
    st.session_state["logado"] = False
    st.rerun()


# -----------------------
# DADOS FAKE
# -----------------------

municipios = [
    "Joinville",
    "Blumenau",
    "Florianópolis",
    "Jaraguá do Sul",
    "Chapecó",
    "Itajaí"
]

categorias = [
    "Saúde",
    "Educação",
    "Infraestrutura",
    "Transporte",
    "Segurança"
]

dados = pd.DataFrame({
    "Município": np.random.choice(municipios, 30),
    "Categoria": np.random.choice(categorias, 30),
    "Valor": np.random.randint(100000, 2000000, 30)
})


# -----------------------
# DASHBOARD
# -----------------------

if pagina == "Dashboard":

    st.title("📊 Dashboard de Despesas Públicas")

    col1, col2, col3 = st.columns(3)

    col1.metric("Municípios Monitorados", "128")
    col2.metric("Despesas Analisadas", "R$ 24.5M")
    col3.metric("Alertas de Irregularidade", "17")

    st.divider()

    st.subheader("📈 Evolução de Gastos Públicos")

    anos = pd.DataFrame({
        "Ano": ["2020", "2021", "2022", "2023", "2024"],
        "Gastos": np.random.randint(5, 20, 5)
    })

    st.line_chart(anos.set_index("Ano"))

    st.divider()

    st.subheader("💰 Distribuição por Categoria")

    categorias_df = dados.groupby("Categoria")["Valor"].sum()

    st.bar_chart(categorias_df)


# -----------------------
# DESPESAS
# -----------------------

if pagina == "Despesas":

    st.title("💰 Despesas Municipais")

    municipio = st.selectbox(
        "Filtrar por Município",
        ["Todos"] + municipios
    )

    if municipio != "Todos":
        df_filtrado = dados[dados["Município"] == municipio]
    else:
        df_filtrado = dados

    st.dataframe(df_filtrado, use_container_width=True)


# -----------------------
# RELATÓRIOS
# -----------------------

if pagina == "Relatórios":

    st.title("📄 Relatórios Financeiros")

    st.write("Exportar dados de despesas municipais.")

    csv = dados.to_csv(index=False)

    st.download_button(
        label="📥 Baixar Relatório CSV",
        data=csv,
        file_name="relatorio_despesas.csv",
        mime="text/csv"
    )

    if st.button("Gerar Relatório Analítico"):
        st.success("Relatório gerado com sucesso!")