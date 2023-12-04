import requests
from bs4 import BeautifulSoup

url = 'https://www.transfermarkt.com.br/flamengo-rio-de-janeiro/startseite/verein/614/saison_id/2022'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontrar a tabela com a classe 'items'
    tabela = soup.find('table', {'class': 'items'})

    # Verificar se a tabela foi encontrada
    if tabela:
        # Encontrar todas as linhas (<tr>) na tabela
        linhas = tabela.find_all('tr')

        # Iterar sobre as linhas e extrair as informações desejadas
        for linha in linhas:
            # Extrair informações das células (<td>) ou cabeçalhos (<th>) se necessário
            celulas = linha.find_all(['td', 'th'])
            
            # Processar e imprimir as informações
            for celula in celulas:
                print(celula.text.strip())

    else:
        print("Tabela 'items' não encontrada.")

else:
    print(f"Erro ao acessar a página. Código de status: {response.status_code}")
