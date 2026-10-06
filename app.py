import streamlit as st
from modulos.crypto_binance import buscar_dados_crypto
from modulos.acoes_yfinance import buscar_dados_acoes
from modulos.portfolio_pessoal import obter_meu_portfolio

st.set_page_config(page_title="Monitor de Fluxo de Capital", layout="wide")

st.title("🚀 Monitor de Fluxo de Capital em Tempo Real")
st.write("Painel central de monitoramento multisseorial de ativos e mercados globais.")

# Criação das abas no Streamlit
aba_crypto, aba_acoes, aba_portfolio = st.tabs(["Criptomoedas", "Ações (Globais/Tech)", "Meu Portefólio XTB"])

with aba_crypto:
    st.subheader("📊 Monitoramento: Criptomoedas")
    dados_crypto = buscar_dados_crypto()
    if dados_crypto:
        cols = st.columns(len(dados_crypto))
        for i, (simbolo, info) in enumerate(dados_crypto.items()):
            with cols[i]:
                st.metric(label=simbolo, value=f"$ {info['preco']:,.2f}", delta=f"{info['variacao']:.2f}%")

with aba_acoes:
    st.subheader("📊 Monitoramento: Ações Globais")
    dados_acoes = buscar_dados_acoes()
    if dados_acoes:
        cols = st.columns(len(dados_acoes))
        for i, (simbolo, info) in enumerate(dados_acoes.items()):
            with cols[i]:
                st.metric(label=simbolo, value=f"$ {info['preco']:,.2f}", delta=f"{info['variacao']:.2f}%")

with aba_portfolio:
    st.subheader("💼 Meu Portefólio Pessoal (XTB / Ativos)")
    meu_portfolio = obter_meu_portfolio()
    
    if meu_portfolio:
        for item in meu_portfolio:
            # Mostra cada ativo do portefólio numa linha detalhada
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.markdown(f"**Ativo:** {item['ticker']}")
                st.text(f"Data Compra: {item['data']}")
            with col2:
                st.markdown(f"**Quantidade:** {item['quantidade']}")
                st.text(f"Preço Entrada: $ {item['preco_entrada']:,.2f}")
            with col3:
                st.markdown(f"**Preço Atual:** $ {item['preco_atual']:,.2f}")
            with col4:
                st.metric(
                    label="Lucro / Prejuízo", 
                    value=f"$ {item['lucro_prejuizo']:,.2f}", 
                    delta=f"{item['variacao_pct']:.2f}%"
                )
            st.divider()

st.info("💡 Atualização ativa: o painel recolhe os dados em tempo real sempre que atualiza a página.")
