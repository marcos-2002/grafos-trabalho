from grafo import Grafo
from arquivo import *

tamanho, arestas = ler_arquivo()
grafo = Grafo(tamanho, arestas)

print('-=-=-=-=-=-=-= Início =-=-=-=-=-=-=-=')
while True:
    print('''
    1 - Ver matriz de adjacência
    2 - Ver lista de adjacência
    3 - Ver componentes do grafo
    4 - Ver vértices pais e seus filhos e os níveis dos vértices
    5 - Ver o caminho mínimo entre dois vértices
    7 - Sair
''')
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    escolha = int(input('Digite sua escolha: '))
    if escolha == 7:
        break
    elif escolha == 1:
        matriz_adjacencia = grafo.getM_adjacencia()
        for x in range(grafo.tamanho):
            print(f'{x+1} - {matriz_adjacencia[x]}')
    elif escolha == 2:
        lista_adjacencia = grafo.getL_adjacencia()
        lista_adjacencia_formatada = list()
        for x in range(grafo.tamanho):
            lista_adjacencia_formatada.append([y + 1 for y in lista_adjacencia[x]])
        for x in range(grafo.tamanho):
            print(f'{x+1} - {lista_adjacencia_formatada[x]}')
    elif escolha == 3:
        grafo.componentes()
    elif escolha == 4:
        familia, nivel = grafo.usar_bfs()
        nivel_formatado = {chave + 1: valor + 1 for chave, valor in nivel.items()}
        print('Família:')
        for x in familia:
            print(f'{x} - {familia[x]}')
        print('Nível: ', nivel_formatado)
    elif escolha == 5:
        caminho = grafo.caminho_minimo()

print('\n-=-=-=-=-=-=-=-= FIM =-=-=-=-=-=-=-=-=\n')

