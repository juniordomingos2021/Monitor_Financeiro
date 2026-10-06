import yfinance as yf

def buscar_dados_acoes():
    """
    Laboratório de Ações (Versão Blindada):
    Usa yfinance de forma segura para extrair preços sem erros de 'nan'.
    """
    simbolos_acoes = ['AAPL', 'MSFT', 'NVDA', 'TSLA']
    resultados_acoes = {}
    
    for simbolo in simbolos_acoes:
        try:
            # Puxa os dados recentes do ativo
            acao = yf.Ticker(simbolo)
            hist = acao.history(period="5d") # Puxa 5 dias para garantir que apanha dias úteis
            
            if not hist.empty and 'Close' in hist.columns:
                # Retira o último preço de fecho válido de forma segura
                preco_atual = float(hist['Close'].dropna().iloc[-1])
                
                # Se houver mais do que um registo, calcula a variação
                if len(hist['Close'].dropna()) >= 2:
                    preco_anterior = float(hist['Close'].dropna().iloc[-2])
                    variacao = ((preco_atual - preco_anterior) / preco_anterior) * 100
                else:
                    variacao = 0.0
                
                resultados_acoes[simbolo] = {
                    'preco': preco_atual,
                    'variacao': variacao
                }
            else:
                resultados_acoes[simbolo] = {'preco': 0.0, 'variacao': 0.0}
                
        except Exception as e:
            print(f"Erro ao processar {simbolo}: {e}")
            resultados_acoes[simbolo] = {'preco': 0.0, 'variacao': 0.0}
            
    return resultados_acoes
