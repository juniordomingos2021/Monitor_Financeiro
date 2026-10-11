import requests

def buscar_dados_crypto():
    """
    Busca preços e variação de 24h na CoinGecko com chaves normalizadas.
    """
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana,binancecoin&vs_currencies=usd&include_24hr_change=true"
    
    try:
        resposta = requests.get(url, timeout=10)
        
        if resposta.status_code == 200:
            dados = resposta.json()
            
            # Usamos chaves idênticas às que o app.py espera
            resultados = {
                'Bitcoin (BTC)': {
                    'preco': float(dados.get('bitcoin', {}).get('usd', 0.0)),
                    'variacao': float(dados.get('bitcoin', {}).get('usd_24h_change', 0.0) or 0.0)
                },
                'Ethereum (ETH)': {
                    'preco': float(dados.get('ethereum', {}).get('usd', 0.0)),
                    'variacao': float(dados.get('ethereum', {}).get('usd_24h_change', 0.0) or 0.0)
                },
                'Solana (SOL)': {
                    'preco': float(dados.get('solana', {}).get('usd', 0.0)),
                    'variacao': float(dados.get('solana', {}).get('usd_24h_change', 0.0) or 0.0)
                },
                'Binance Coin (BNB)': {
                    'preco': float(dados.get('binancecoin', {}).get('usd', 0.0)),
                    'variacao': float(dados.get('binancecoin', {}).get('usd_24h_change', 0.0) or 0.0)
                }
            }
            return resultados
        else:
            print(f"Erro na API CoinGecko: Status {resposta.status_code}")
            return None
            
    except Exception as e:
        print(f"Erro de ligação: {e}")
        return None
