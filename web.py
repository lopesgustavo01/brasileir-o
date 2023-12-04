'''
Script responsavel por fazer rapagem de dados
Pegar informaçoes das rodadas

'''


import requests, re, json
from bs4 import BeautifulSoup

def limpar_lista(lista):
    # Primeiro padrão
    padrao = re.compile(r'(\d{2}/\d{2} \d{2}:\d{2})\n• (.+)\n\n\n\n\n(.+)\n\n\n\n\n(\d+)\n\n(\d+)\n\n\n\n\n(.+)')
    resultados = padrao.match(lista)

    # Verificar se houve correspondência com o primeiro padrão
    if resultados:
        # Extrair os grupos correspondentes
        data_hora = resultados.group(1)
        local = resultados.group(2)
        time_casa = resultados.group(3)
        placar_casa = resultados.group(4)
        placar_fora = resultados.group(5)
        time_fora = resultados.group(6)
    else:
        # Segundo padrão
        padrao2 = re.compile(r'(\d{2}/\d{2} \d{2}:\d{2})\n• (.+?)\n+(\S+)\n+(\d+)?\n+(\d+)?\n+(\S+)?')
        resultados = padrao2.match(lista)

        # Verificar se houve correspondência com o segundo padrão
        if resultados:
            # Extrair os grupos correspondentes
            data_hora = resultados.group(1)
            local = resultados.group(2)
            time_casa = resultados.group(3)

            # Verificar se há placar para o time da casa
            placar_casa = resultados.group(4) if resultados.group(4) else 'Sem placar'

            # Verificar se há placar para o time visitante
            placar_fora = resultados.group(5) if resultados.group(5) else 'Sem placar'

            # Verificar se há time visitante
            time_fora = resultados.group(6) if resultados.group(6) else 'Sem time adversário'
        else:
            print("Nenhum padrão corresponde à linha fornecida.")
            return None

    # Criar a lista desejada
    lista_limpa = {'data': data_hora,'local': local,'time casa': time_casa, 'placar casa': placar_casa,'placar fora': placar_fora, 'time fora': time_fora}

    return lista_limpa

url = "https://www.gazetaesportiva.com/campeonatos/brasileiro-serie-a/"
response = requests.get(url)
jogo_info_list = []
lista_jogos_web = []
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Substitua 'table__games' pelo nome real da classe da tabela desejada
    table_games_ul_list = soup.find_all('ul', class_='table__games')

    if table_games_ul_list:
        jogo_info_list = []

        for table_games_ul in table_games_ul_list:
            # Encontrou uma ul com a classe 'table__games', agora encontre todas as tags 'li' dentro dela
            li_tags = table_games_ul.find_all('li')

            jogo_info = []
            for li_tag in li_tags:
                # Adicione o texto da tag 'li' à lista jogo_info
                jogo_info.append(li_tag.text.strip())

            # Adicione a lista jogo_info à lista jogo_info_list
            jogo_info_list.append(jogo_info)

        # Imprima a lista final
        for jogo_info in jogo_info_list:
            lista_jogos_web.append(jogo_info)
    else:
        print("Nenhuma ul com a classe 'table__games' encontrada no HTML.")
else:
    print(f"Erro ao acessar a página. Código de status: {response.status_code}")



with open('./static/json/rodadas.json', 'w') as json_file:
    json_file.write('{"rodadas": [')
    # Escreve cada rodada diretamente no arquivo JSON
    cont = 1
    for dados_jogo in lista_jogos_web:
        rodada = {'rodada': cont, 'jogos': []}
        cont += 1
        for i in dados_jogo:
            partida = limpar_lista(i)
            rodada['jogos'].append(partida)
        json.dump(rodada, json_file, indent=2)
        if cont <= 38:
            json_file.write(',')
    json_file.write(']}')




