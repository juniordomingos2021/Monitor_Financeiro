import yfinance as yf

def obter_meu_portfolio():
    """
    Laboratório de Portefólio Pessoal:
    Regista as suas compras reais (ativo, preço de entrada, quantidade, data)
    e calcula em tempo real o valor atual e a variação face ao preço de compra.
    """
    
    # Simula o seu "diário de bordo" de compras (o seu portefólio pessoal)
    # No futuro, podemos ligar isto a um campo para você digitar novas compras na tela!
    minhas_compras = [
        {"ticker": "AAPL", "quantidade": 10, "preco_entrada": 175.50, "data": "2026-02-10"},
        {"ticker": "MSFT", "quantidade": 5, "preco_entrada": 410.00, "data": "2026-03-01"},
        {"ticker": "NVDA", "quantidade": 8, "preco_entrada": 850.25, "data": "2026-03-15"}
    ]
    
    portfolio_atualizado = []
    
    for item in minhas_compras:
        ticker = item["ticker"]
        qtd = item["quantidade"]
        preco_compra = item["preco_entrada"]
        data_compra = item["data"]
        
        try:
            # Vai buscar o preço atualizado à web (via yfinance)
            acao = yf.Ticker(ticker)
            hist = acao.history(period="1d")
            
            if not hist.empty and 'Close' in hist.columns:
                preco_atual = float(hist['Close'].dropna().iloc[-1])
            else:
                preco_atual = preco_compra # Fallback caso falhe
                
            # Cálculos financeiros do portefólio
            valor_investido = qtd * preco_compra
            valor_atual = qtd * preco_atual
            lucro_prejuizo = valor_atual - valor_investido
            variacao_pct = ((preco_atual - preco_compra) / preco_compra) * 100
            
            # Guarda o resultado processado
            portfolio_atualizado.append({
                "ticker": ticker,
                "quantidade": qtd,
                "preco_entrada": preco_compra,
                "preco_atual": preco_atual,
                "data": data_compra,
                "valor_investido": valor_investido,
                "valor_atual": valor_atual,
                "lucro_prejuizo": lucro_prejuizo,
                "variacao_pct": variacao_pct
            })
            
        except Exception as e:
            print(f"Erro ao calcular portefólio para {ticker}: {e}")
            
    return portfolio_atualizado
