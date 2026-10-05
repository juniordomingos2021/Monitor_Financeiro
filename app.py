import streamlit as st
import requests

# Configuração básica da página
st.set_page_config(page_title="Monitor de Capital", page_icon="📈", layout="wide")

st.title("🚀 Monitor de Fluxo de Capital em Tempo Real")
st.write("Painel central de monitoramento de ativos, criptomoedas e mercado financeiro.")

st.markdown("---")

st.header("🪙 Monitor de Criptomoedas (Dados Oficiais da Binance)")
st.write("Cotações em tempo real conectadas diretamente à alta liquidez do mercado.")

# Pares oficiais na Binance (Mercado Spot)
simbolos = {
    "Bitcoin (BTC)": "BTCUSDT",
    "Ethereum (ETH)": "ETHUSDT",
    "Solana (SOL)": "SOLUSDT"
}

col1, col2, col3 = st.columns(3)
colunas = [col1, col2, col3]

# Função para buscar o preço direto na API pública da Binance
def obter_preco_binance(symbol):
    try:
        url = f"https://api.binance.com/api/v3/ticker/24hr?symbol={symbol}"
        resposta = requests.get(url, timeout=5)
        if resposta.status_code == 200:
            dados = resposta.json()
            preco_atual = float(dados['lastPrice'])
            variacao = float(dados['priceChangePercent'])
            return preco_atual, variacao
    except Exception as e:
        pass
    return None, None

# Renderizar os dados nas colunas
for i, (nome, ticker) in enumerate(simbolos.items()):
    with colunas[i]:
        preco, variacao = obter_preco_binance(ticker)
        
        if preco is not None:
            st.metric(
                label=nome,
                value=f"$ {preco:,.2f}",
                delta=f"{variacao:.2f}%"
            )
        else:
            st.warning(f"Erro ao conectar com a Binance para {nome}")

st.markdown("---")
st.info("💡 Dados sincronizados em tempo real com a liquidez global da Binance.")
