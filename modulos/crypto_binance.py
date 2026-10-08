import ccxt

def buscar_dados_crypto():
    """
    Laboratório de Criptomoedas:
    Usa a biblioteca ccxt para buscar preços em tempo real na Binance.
    """
    try:
        exchange = ccxt.binance()
        simbolos = ['BTC/USDT', 'ETH/USDT', 'SOL/USDT', 'BNB/USDT']
        
        resultados = {}
        
        for simbolo in simbolos:
            ticker = exchange.fetch_ticker(simbolo)
            preco = ticker['last']
            
            # Tenta calcular a variação de 24h se disponível, senão assume 0
            variacao = ticker.get('percentage', 0.0)
            if variacao is None:
                variacao = 0.0
                
            # Simplifica o nome para mostrar no painel (ex: BTC/USDT vira BTC)
            nome_limpo = simbolo.split('/')[0]
            if nome_limpo == 'BTC':
                nome_limpo = 'Bitcoin (BTC)'
            elif nome_limpo == 'ETH':
                nome_limpo = 'Ethereum (ETH)'
            elif nome_limpo == 'SOL':
                nome_limpo = 'Solana (SOL)'
            elif nome_limpo == 'BNB':
                nome_limpo = 'Binance Coin (BNB)'
                
            resultados[nome_limpo] = {
                'preco': float(preco),
                'variacao': float(variacao)
            }
            
        return resultados
    except Exception as e:
        print(f"Erro ao buscar criptos: {e}")
        return None
