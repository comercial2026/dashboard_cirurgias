import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from fpdf import FPDF
from datetime import datetime

st.set_page_config(page_title="Dashboard de Cirurgias", layout="wide")

# ========================
# 🔒 LOGIN
# ========================
users = {
    "thania": "123",
    "fabia": "456",
    "everton": "789",
    "welba": "abc",
    "patricia": "def",
    "mileni": "ghi"
}

# Inicializa variáveis de sessão
if 'login' not in st.session_state:
    st.session_state['login'] = False
if 'user' not in st.session_state:
    st.session_state['user'] = None

# Se ainda não fez login → mostra tela de login
if not st.session_state['login']:
    st.title("🔒 Login")
    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")

    login_button = st.button("Entrar")

    if login_button:
        if username.lower() in users and users[username.lower()] == password:
            st.session_state['login'] = True
            st.session_state['user'] = username.capitalize()
            st.success(f"Bem-vindo(a), {username.capitalize()}!")
            st.rerun()  # 🔁 recarrega a página logada
        else:
            st.error("Usuário ou senha incorretos")

    # Interrompe a execução aqui enquanto o login não for feito
    st.stop()

# Se o usuário já estiver logado → mostra botão de logout
else:
    with st.sidebar:
        st.success(f"✅ Logado como {st.session_state['user']}")
        if st.button("Sair"):
            st.session_state['login'] = False
            st.session_state['user'] = None
            st.rerun()



# ========================
# 🔹 CARREGAR DADOS
# ========================
@st.cache_data(ttl=3600)
def carregar_dados():
    try:
        df = pd.read_excel("data/cirurgias.xlsx")
    except:
        # Gerar dados de exemplo se não houver arquivo
        np.random.seed(42)
        vendedores = ["Thania","Fábia","Everton","Welba","Patricia","Mileni"]
        medicos = ["Dr. Silva","Dra. Costa","Dr. Pereira","Dra. Almeida","Dr. Ramos","Dra. Santos"]
        procedimentos = ["Artroscopia","Histerectomia","Colecistectomia","Catarata","Hernioplastia","Laparoscopia"]
        cidades_estados = [
    ("São Paulo", "SP"),
    ("Rio de Janeiro", "RJ"),
    ("Belo Horizonte", "MG"),
    ("Recife", "PE"),
    ("Curitiba", "PR"),
    ("Porto Alegre", "RS"),
    ("Fortaleza", "CE"),
    ("Brasília", "DF"),
    ("Salvador", "BA")
]
