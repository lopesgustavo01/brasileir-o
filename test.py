import json

def rod(num):
    # Nome do arquivo JSON
    nome_arquivo = './static/json/rodadas.json'

    # Abre o arquivo JSON para leitura
    with open(nome_arquivo, 'r') as json_file:
        # Carrega os dados do arquivo JSON
        dados = json.load(json_file)

    # Agora, 'dados' contém a estrutura do seu arquivo JSON
    return dados['rodadas'][num]