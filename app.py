import streamlit as st
import yfinance as yf

# Configuração básica da página
st.set_page_config(page_title="Monitor de Capital", page_icon="📈", layout="wide")

st.title("🚀 Monitor de Fluxo de Capital em Tempo Real")
st.write("Painel central de monitoramento de ativos, criptomoedas e mercado financeiro.")

# Divisor visual
st.markdown("---")

st.header("🪙 Monitor de Criptomoedas (BTC, ETH, SOL)")
st.write("Acompanhamento em tempo real das principais criptomoedas do mercado.")

# Dicionário com os ativos que queremos monitorar
criptos = {
    "Bitcoin (BTC)": "BTC-USD",
    "Ethereum (ETH)": "ETH-USD",
    "Solana (SOL)": "SOL-USD"
}

# Criamos colunas lado a lado na tela
col1, col2, col3 = st.columns(3)
colunas = [col1, col2, col3]

# Buscamos os dados de cada criptomoeda e exibimos no painel
for i, (nome, ticker) in enumerate(criptos.items()):
    with colunas[i]:
        try:
            # Puxa os dados do dia atual do Yahoo Finance
            dados = yf.Ticker(ticker)
            hist = dados.history(period="1d")
            
            if not hist.empty:
                preco_atual = hist['Close'].iloc[-1]
                preco_abertura = hist['Open'].iloc[0]
                variacao = ((preco_atual - preco_abertura) / preco_abertura) * 100
                
                # Mostra um bloco visual bonito com o preço e a variação percentual
                st.metric(
                    label=nome, 
                    value=f"$ {preco_atual:,.2f}", 
                    delta=f"{variacao:.2f}%"
                )
            else:
                st.warning(f"Dados indisponíveis para {nome}")
        except Exception as e:
            st.error(f"Erro ao carregar {nome}")

st.markdown("---")
st.info("💡 Dica: Atualize a página do navegador para buscar as cotações mais recentes do mercado.")
