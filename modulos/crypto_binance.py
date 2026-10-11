import yfinance as yf

def buscar_dados_crypto():
    """
    Laboratório de Criptomoedas (Via yfinance):
    Usa o Yahoo Finance para puxar cotações globais de criptomoedas de forma
    estável e livre de bloqueios de IP em servidores na nuvem.
    """
    # Tickers de criptomoedas no Yahoo Finance
    simbolos = {
        'Bitcoin (BTC)': 'BTC-USD',
        'Ethereum (ETH)': 'ETH-USD',
        'Solana (SOL)': 'SOL-USD',
        'Binance Coin (BNB)': 'BNB-USD'
    }
    
    resultados = {}
    
    for nome_limpo, simbolo in simbolos.items():
        try:
            # Puxa os dados recentes do ativo no Yahoo Finance
            crypto = yf.Ticker(simbolo)
            hist = crypto.history(period="2d")
            
            if not hist.empty and 'Close' in hist.columns:
                preco_atual = float(hist['Close'].dropna().iloc[-1])
                
                # Calcula a variação diária se houver pelo menos 2 dias de histórico
                if len(hist['Close'].dropna()) >= 2:
                    preco_anterior = float(hist['Close'].dropna().iloc[-2])
                    variacao = ((preco_atual - preco_anterior) / preco_anterior) * 100
                else:
                    variacao = 0.0
            else:
                preco_atual = 0.0
                variacao = 0.0
                
            resultados[nome_limpo] = {
                'preco': preco_atual,
                'variacao': variacao
            }
            
        except Exception as e:
            print(f"Erro ao buscar {nome_limpo} via yfinance: {e}")
            resultados[nome_limpo] = {'preco': 0.0, 'variacao': 0.0}
            
    return resultados
