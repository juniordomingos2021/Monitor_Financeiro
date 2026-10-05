import streamlit as st
import requests
import time

# Configuração básica da página
st.set_page_config(page_title="Monitor de Capital", page_icon="📈", layout="wide")

st.title("🚀 Monitor de Fluxo de Capital em Tempo Real")
st.write("Painel central de monitoramento de ativos, criptomoedas e mercado financeiro.")

st.markdown("---")

st.header("🪙 Monitor de Criptomoedas (Referência Oficial Binance)")
st.write("Cotações em tempo real conectadas diretamente à alta liquidez global.")

# Pares de ativos na Binance
pares = {
    "Bitcoin (BTC)": "BTCUSDT",
    "Ethereum (ETH)": "ETHUSDT",
    "Solana (SOL)": "SOLUSDT"
}

col1, col2, col3 = st.columns(3)
colunas = [col1, col2, col3]

def buscar_preco_binance(symbol):
    try:
        url = f"https://data-api.binance.vision/api/v3/ticker/24hr?symbol={symbol}"
        headers = {'User-Agent': 'Mozilla/5.0'}
        resposta = requests.get(url, headers=headers, timeout=5)
        
        if resposta.status_code == 200:
            dados = resposta.json()
            preco = float(dados['lastPrice'])
            variacao = float(dados['priceChangePercent'])
            return preco, variacao
    except Exception as e:
        pass
    return None, None

# Renderizar os dados nas colunas
for i, (nome, ticker) in enumerate(pares.items()):
    with colunas[i]:
        preco, variacao = buscar_preco_binance(ticker)
        
        if preco is not None:
            st.metric(
                label=nome,
                value=f"$ {preco:,.2f}",
                delta=f"{variacao:.2f}%"
            )
        else:
            st.warning(f"A sincronizar {nome}...")

st.markdown("---")
st.info("💡 Atualização automática ativada: os dados são renovados a cada 5 segundos.")

# --- SISTEMA DE ATUALIZAÇÃO AUTOMÁTICA A CADA 5 SEGUNDOS ---
time.sleep(1)
st.rerun()
