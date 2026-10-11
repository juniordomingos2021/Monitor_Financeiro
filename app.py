with aba_crypto:
    st.subheader("📊 Monitoramento: Criptomoedas")
    dados_crypto = buscar_dados_crypto()
    
    if dados_crypto:
        cols = st.columns(len(dados_crypto))
        for i, (simbolo, info) in enumerate(dados_crypto.items()):
            with cols[i]:
                st.metric(
                    label=simbolo, 
                    value=f"$ {info['preco']:,.2f}", 
                    delta=f"{info['variacao']:.2f}%"
                )
    else:
        st.warning("A carregar dados de criptomoedas ou a aguardar resposta da API...")
