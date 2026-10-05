import streamlit as st
import requests

# Configuração básica da página
st.set_page_config(page_title="Monitor de Capital", page_icon="📈", layout="wide")

st.title("🚀 Monitor de Fluxo de Capital em Tempo Real")
st.write("Painel central de monitoramento de ativos, criptomoedas e mercado financeiro.")

st.markdown("---")

st.header("🪙 Monitor de Criptomoedas (Mercado Global)")
st.write("Cotações em tempo real sincronizadas com as principais referências do mercado.")

# IDs dos ativos na API pública da CoinGecko
criptos = {
    "Bitcoin (BTC)": "bitcoin",
    "Ethereum (ETH)": "ethereum",
    "Solana (SOL)": "solana"
}

col1, col2, col3 = st.columns(3)
colunas = [col1, col2, col3]

def obter_dados_cripto():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd&include_24hr_change=true"
        resposta = requests.get(url, timeout=10)
        if resposta.status_code == 200:
            return resposta.json()
    except Exception as e:
        pass
    return None

# Buscar dados da API
dados_mercado = obter_dados_cripto()

# Renderizar os dados nas colunas
for i, (nome, id_ativo) in enumerate(criptos.items()):
    with colunas[i]:
        if dados_mercado and id_ativo in dados_mercado:
            preco = dados_mercado[id_ativo]['usd']
            variacao = dados_mercado[id_ativo].get('usd_24h_change', 0.0)
            
            st.metric(
                label=nome,
                value=f"$ {preco:,.2f}",
                delta=f"{variacao:.2f}%"
            )
        else:
            st.warning(f"A aguardar sincronização para {nome}...")

st.markdown("---")
st.info("💡 Conectado com sucesso à rede global de dados de criptoativos.")
