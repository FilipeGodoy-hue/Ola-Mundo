import requests

def buscar_cotacao(moeda):
    # Endpoint da AwesomeAPI para buscar Dólar para Real
    url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
    
    try:
        response = requests.get(url)
        dados = response.json()
        
        # O JSON retorna uma chave como 'USDBRL', por isso acessamos assim:
        chave = f"{moeda}BRL"
        cotacao = dados[chave]['bid']
        return float(cotacao)
    except Exception as e:
        print(f"Erro ao buscar cotação: {e}")
        return None

# Interface simples
print("--- Conversor de Moedas Real-Time ---")
moeda_escolhida = input("Qual moeda quer converter para Real? (Ex: USD, EUR, BTC): ").upper()
valor_estrangeiro = float(input(f"Quanto você tem em {moeda_escolhida}? "))

taxa = buscar_cotacao(moeda_escolhida)

if taxa:
    # Cálculo simples: Valor em Real = Valor Estrangeiro * Taxa de Câmbio
    valor_real = valor_estrangeiro * taxa
    print(f"Cotação atual: R$ {taxa:.2f}")
    print(f"Você teria: R$ {valor_real:.2f}")
