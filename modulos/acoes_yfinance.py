import yfinance as yf

def buscar_dados_acoes():
    """
    Laboratório de Ações:
    Usa a biblioteca yfinance para puxar os preços e calcular variações diárias
    das principais empresas tecnológicas do mercado global.
    """
    try:
        # Lista de tickers de ações globais
        simbolos_acoes = ['AAPL', 'MSFT', 'NVDA', 'TSLA']
        
        resultados_acoes = {}
        
        for simbolo in simbolos_acoes:
            # Puxa o objeto do ativo
            acao = yf.Ticker(simbolo)
            
            # Puxa o histórico dos últimos 2 dias para calcular a variação
            hist = acao.history(period="2d")
            
            if len(hist) >= 1:
                # Preço de fecho mais recente
                preco_atual = float(hist['Close'].iloc[-1])
                
                # Se houver pelo menos 2 dias, calcula a variação percentual
                if len(hist) >= 2:
                    preco_anterior = float(hist['Close'].iloc[-2])
                    variacao = ((preco_atual - preco_anterior) / preco_anterior) * 100
                else:
                    variacao = 0.0
                
                resultados_acoes[simbolo] = {
                    'preco': preco_atual,
                    'variacao': variacao
                }
                
        return resultados_acoes
    except Exception as e:
        print(f"Erro ao consultar yfinance para ações: {e}")
        return None
