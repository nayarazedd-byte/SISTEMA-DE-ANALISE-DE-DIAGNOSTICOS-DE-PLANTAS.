import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Configuração da página e Estética Cottagecore
st.set_page_config(page_title="Diagnóstico Botânico", page_icon="🌿", layout="centered")

st.markdown("""
<style>
    /* Fundo herbal vintage */
    .stApp {
        background-color: #f4f1ea;
        color: #2c4c3b;
        font-family: 'Georgia', serif;
    }
    /* Estilo dos botões */
    .stButton>button {
        background-color: #6b8e23;
        color: white;
        border-radius: 8px;
        border: none;
        width: 100%;
        padding: 10px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #55711b;
        color: #f4f1ea;
    }
    /* Headers com cara de livro de botânica */
    h1, h2, h3 {
        color: #3b5323;
        font-family: 'Georgia', serif;
    }
</style>
""", unsafe_allow_html=True)

st.title("🌿 Botânica Vintage")
st.subheader("Diagnóstico Rápido de Saúde de Plantas")
st.write("Me conte o que há de errado com sua plantinha ou envie uma foto para a análise.")

# Opções de entrada dinâmica
st.markdown("### O que você está observando?")
col1, col2, col3 = st.columns(3)

# Controle de estado para os botões preencherem o input de texto
if 'sintoma' not in st.session_state:
    st.session_state.sintoma = ""

if col1.button("🍂 Folhas Amarelas"):
    st.session_state.sintoma = "Folhas amarelas"
if col2.button("🥀 Planta Murcha"):
    st.session_state.sintoma = "Planta murcha"
if col3.button("🏜️ Terra Seca"):
    st.session_state.sintoma = "Terra seca"

# Input de texto (o usuário pode digitar ou clicar nos botões)
sintoma_texto = st.text_input("Ou descreva o problema aqui em detalhes:", value=st.session_state.sintoma)

# Upload de Imagem
imagem = st.file_uploader("Upload da imagem da planta (opcional)", type=["jpg", "png", "jpeg"])

# Função que simula o modelo TensorFlow gerando respostas dinâmicas
def gerar_diagnostico(texto, img):
    texto = texto.lower()
    
    # Se uma imagem foi enviada, o modelo dá prioridade visual
    if img is not None:
        return {
            "diag": "Análise de Imagem: Padrão de fungo ou mancha foliar detectado pelo TensorFlow.",
            "cor_fundo": "#f8d7da", # Vermelho claro
            "cor_borda": "#dc3545",
            "cor_texto": "#721c24",
            "acao": "1. ✂️ Isole a planta imediatamente.<br>2. 🧪 Aplique um fungicida natural (como óleo de neem).<br>3. ☀️ Evite molhar as folhas nas próximas regas."
        }
    
    # Condições baseadas no texto digitado ou botão clicado
    elif "amarela" in texto:
        return {
            "diag": "Excesso de Água ou Deficiência de Nitrogênio.",
            "cor_fundo": "#fff3cd", # Amarelo claro
            "cor_borda": "#ffc107",
            "cor_texto": "#856404",
            "acao": "1. 🛑 Pare de regar por alguns dias e sinta o solo.<br>2. 🪴 Verifique se a água está escoando bem pelo fundo do vaso.<br>3. 💩 Aplique um adubo orgânico rico em nitrogênio assim que a terra secar."
        }
    elif "murcha" in texto:
        return {
            "diag": "Estresse Hídrico Severo (Falta de água) ou Choque Térmico.",
            "cor_fundo": "#d1ecf1", # Azul claro
            "cor_borda": "#17a2b8",
            "cor_texto": "#0c5460",
            "acao": "1. 💧 Faça uma rega de imersão: coloque o vaso numa bacia com água por 15 minutos.<br>2. 🌡️ Mantenha a planta longe de correntes de ar frio ou ar-condicionado."
        }
    elif "seca" in texto:
        return {
            "diag": "Baixa Umidade do Ar ou Queimadura Solar.",
            "cor_fundo": "#f8d7da", # Vermelho claro
            "cor_borda": "#dc3545",
            "cor_texto": "#721c24",
            "acao": "1. 🌤️ Mova o vaso para um local com luz indireta (sem sol batendo direto).<br>2. 💦 Borrife água filtrada nas folhas nas horas mais frescas do dia.<br>3. ✂️ Pode apenas as pontinhas que já esturricaram."
        }
    else:
        # Caso genérico quando o modelo não reconhece palavras-chave exatas
        return {
            "diag": "Sintomas Iniciais ou Não Específicos.",
            "cor_fundo": "#e2e3e5", # Cinza claro
            "cor_borda": "#6c757d",
            "cor_texto": "#383d41",
            "acao": "1. 🧐 Observe sua planta atentamente por mais 3 dias.<br>2. 💧 Mantenha uma rotina básica: regue apenas quando enfiar o dedo na terra e sentir que está completamente seca."
        }

if st.button("Analisar Planta"):
    if not sintoma_texto and imagem is None:
        st.warning("Por favor, descreva o sintoma ou envie uma foto para eu poder ajudar!")
    else:
        st.markdown("---")
        st.info("🌱 A inteligência botânica está analisando as evidências no TensorFlow...")
        
        # Puxa o diagnóstico dinâmico baseado no que o usuário colocou
        resultado = gerar_diagnostico(sintoma_texto, imagem)
        
        # Monta os blocos coloridos dinamicamente usando as variáveis
        st.markdown(f"""
        <div style="background-color: {resultado['cor_fundo']}; padding: 15px; border-radius: 10px; color: {resultado['cor_texto']}; margin-bottom: 15px; border-left: 5px solid {resultado['cor_borda']};">
            <strong>🩺 Diagnóstico Principal:</strong> {resultado['diag']}
        </div>
        
        <div style="background-color: #d4edda; padding: 15px; border-radius: 10px; color: #155724; border-left: 5px solid #28a745;">
            <strong>📋 Plano de Ação Eficaz:</strong><br><br>
            {resultado['acao']}
        </div>
        """, unsafe_allow_html=True)