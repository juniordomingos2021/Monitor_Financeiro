import streamlit as st
import requests
import yfinance as yf
import time
from config_ativos import ATIVOS_MERCADO

# Configuração básica da página
st.set_page_config(page_title="Monitor de Capital", page_icon="📈", layout="wide")

st.title("🚀 Monitor de Fluxo de Capital em Tempo Real")
st.write("Painel central de monitoramento multisseorial de ativos e mercados globais.")

st.markdown("---")

# Criamos abas dinâmicas baseadas nas categorias do nosso ficheiro de configuração
categorias = list(ATIVOS_MERCADO.keys())
abas = st.tabs([f"📂 {cat}" for cat in categorias])

# Função para buscar dados de cripto (Binance)
def buscar_preco_binance(symbol):
    try:
        url = f"https://data-api.binance.vision/api/v3/ticker/24hr?symbol={symbol}"
        headers = {'User-Agent': 'Mozilla/5.0'}
        resposta = requests.get(url, headers=headers, timeout=4)
        if resposta.status_code == 200:
            dados = resposta.json()
            return float(dados['lastPrice']), float(dados['priceChangePercent'])
    except:
        pass
    return None, None

# Função para buscar dados gerais (Ações, Forex, B3, Commodities via yfinance)
def buscar_preco_yfinance(symbol):
    try:
        dados = yf.Ticker(symbol)
        hist = dados.history(period="2d")
        if len(hist) >= 1:
            preco_atual = hist['Close'].iloc[-1]
            if len(hist) >= 2:
                preco_anterior = hist['Close'].iloc[-2]
                variacao = ((preco_atual - preco_anterior) / preco_anterior) * 100
            else:
                variacao = 0.0
            return float(preco_atual), float(variacao)
    except:
        pass
    return None, None

# Preencher cada aba com os seus respetivos ativos
for idx, categoria in enumerate(categorias):
    with abas[idx]:
        st.subheader(f"📊 Monitoramento: {categoria}")
        ativos_da_categoria = ATIVOS_MERCADO[categoria]
        
        # Criar colunas para os ativos da categoria
        cols = st.columns(len(ativos_da_categoria))
        
        for i, (nome, ticker) in enumerate(ativos_da_categoria.items()):
            with cols[i]:
                # Se for cripto, usa a API da Binance; caso contrário, usa o yfinance
                if categoria == "Criptomoedas":
                    preco, variacao = buscar_preco_binance(ticker)
                else:
                    preco, variacao = buscar_preco_yfinance(ticker)
                
                if preco is not None:
                    st.metric(
                        label=nome,
                        value=f"$ {preco:,.2f}" if categoria != "B3 (Brasil)" else f"R$ {preco:,.2f}",
                        delta=f"{variacao:.2f}%"
                    )
                else:
                    st.warning(f"A carregar {nome}...")

st.markdown("---")
st.info("💡 Atualização automática ativada: o painel renova os dados de todos os mercados a cada 5 segundos.")

# --- ATUALIZAÇÃO AUTOMÁTICA A CADA 5 SEGUNDOS ---
time.sleep(5)
st.rerun()
