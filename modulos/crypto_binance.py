import ccxt

def buscar_dados_crypto():
    """
    Laboratório de Criptomoedas (Versão Blindada com Fallback):
    Tenta ligar à Binance via ccxt. Se a rede falhar ou bloquear o IP na nuvem,
    utiliza valores de segurança para que o painel nunca fique vazio.
    """
    simbolos = ['BTC/USDT', 'ETH/USDT', 'SOL/USDT', 'BNB/USDT']
    resultados = {}
    
    try:
        exchange = ccxt.binance({
            'enableRateLimit': True,
            'options': {'defaultType': 'spot'}
        })
        
        for simbolo in simbolos:
            try:
                ticker = exchange.fetch_ticker(simbolo)
                preco = float(ticker.get('last', 0.0))
                variacao = float(ticker.get('percentage', 0.0) or 0.0)
            except Exception:
                # Fallback individual caso falhe um ativo específico
                precos_fallback = {
                    'BTC/USDT': 85528.00, 
                    'ETH/USDT': 2704.77, 
                    'SOL/USDT': 120.50, 
                    'BNB/USDT': 780.62
                }
                preco = precos_fallback.get(simbolo, 1000.0)
                variacao = 0.0
                
            # Formatação do nome
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
                'preco': preco,
                'variacao': variacao
            }
            
        return resultados
        
    except Exception as e:
        print(f"Erro geral ao ligar à Binance: {e}")
        # Fallback total de segurança para o painel nunca falhar
        return {
            'Bitcoin (BTC)': {'preco': 85528.00, 'variacao': -1.25},
            'Ethereum (ETH)': {'preco': 2704.77, 'variacao': -1.04},
            'Solana (SOL)': {'preco': 120.50, 'variacao': -0.91},
            'Binance Coin (BNB)': {'preco': 780.62, 'variacao': -3.59}
        }
