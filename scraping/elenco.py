# import requests
# from bs4 import BeautifulSoup
# import json

# #elenco

# elenco = []

# url = 'https://footystats.org/pt/clubs/ec-bahia-626'

# # Adicionar um User-Agent ao cabeçalho da solicitação
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

# # Obter o conteúdo da página
# response = requests.get(url, headers=headers)
# print(response)
# html = response.text

# # Analisar o HTML com BeautifulSoup
# soup = BeautifulSoup(html, 'html.parser')

# # Encontrar todas as divs com a classe 'w100'
# divs_w100 = soup.find_all('div', class_='w100')

# # Iterar sobre as divs com a classe 'w100'
# for div_w100 in divs_w100:
#     # Encontrar todas as divs com a classe 'w94' dentro da div_w100
#     divs_w94 = div_w100.find_all('div', class_='w94')

#     # Iterar sobre as divs com a classe 'w94'
#     for div_w94 in divs_w94:
#         # Encontrar todos os links com a classe 'semi-bold' dentro da div_w94
#         links_semi_bold = div_w94.find_all('a', class_='semi-bold')
#         for link in links_semi_bold:
#             elenco.append(link.text.strip())
#             print("Texto do link com a classe 'semi-bold':", link.text.strip())



# def adicionar_elenco(json_file, time, lista_nomes):
#     # Carrega o conteúdo atual do arquivo JSON, se existir
#     try:
#         with open(json_file, 'r') as file:
#             dados = json.load(file)
#     except FileNotFoundError:
#         # Se o arquivo não existir, cria uma estrutura inicial
#         dados = {'elencos': []}

#     # Procura se já existe um elenco para o time especificado
#     for elenco in dados['elencos']:
#         if elenco['time'] == time:
#             # Se o time já existe, adiciona os nomes ao elenco existente
#             elenco['elenco'].extend(lista_nomes)
#             break
#     else:
#         # Se o time não existe, cria um novo elenco
#         novo_elenco = {'time': time, 'elenco': lista_nomes}
#         dados['elencos'].append(novo_elenco)

#     # Salva as alterações de volta no arquivo JSON
#     with open(json_file, 'w') as file:
#         json.dump(dados, file, indent=2)

# # Exemplo de uso
# nome_arquivo = './static/json/elenco.json'
# time_cruzeiro = 'Bahia'


# adicionar_elenco(nome_arquivo, time_cruzeiro, elenco)
