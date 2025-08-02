"""
Projeto: Ranking de Jogadores de Futebol 🥅⚽

Este script coleta o nome de jogadores e registra quantos gols
cada um fez em várias partidas. Depois, exibe uma tabela com as informações
de cada jogador: nome, gols por partida e total de gols.

Ideal para treinar uso de listas, dicionários e manipulação de dados com Python.

Autor: deyvison55d
"""

dados = dict()
dados_total = list()
golps = list()
total = 0
while True:
    nome = input('Nome do jogador: ').strip()
    partidas = int(input(f'Quantas partidas {nome} jogou? '))

    for c in range(0, partidas):
        gol = int(input(f'Quantos gols na partida {c}? '))

        golps.append(gol)
        total += gol
    dados['nome'] = nome;
    dados['gols'] = golps[:];
    dados['total'] = total
    dados_total.append(dados.copy())
    golps.clear()
    total = 0

    continuar = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break

print('-='*25)
print(f'{'cod':<5} {'nome':<15} {'gols':<15} {'total':>8}')
for chave, valor in enumerate(dados_total):
    print(f'{chave:<5} '
          f'{dados_total[chave]['nome']:<15} '
          f'{dados_total[chave]['gols']} '
          f'{dados_total[chave]['total']:>15}')

while True:
    mostrar_dados = int(input('Mostrar dados de qual jogador? '))
    print('-'*40)

    if mostrar_dados == 999:
        print('FINALIZANDO...\nVolte sempre!')
        break

    if mostrar_dados > len(dados_total)-1 or mostrar_dados == '':
        print(f'Error! Não existe jogador com código {mostrar_dados}')
        print('-'*40)
        continue

    print(f' -- LEVANTAMENTO DO JOGADOR {dados_total[mostrar_dados]['nome']}:')
    for c in range(0, len(dados_total[mostrar_dados]['gols'])):
        print(f'No jogo {c} fez {dados_total[mostrar_dados]['gols'][c]} gols')
