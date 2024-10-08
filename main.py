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
        vertice_inicial = int(input('Digite o vértice inicial: '))
        vertice_final = int(input('Digite o vértice final: '))
        # Para grafos com pesos
        if any(len(aresta) == 3 for aresta in grafo.getAresta()):
            distances, predecessores = grafo.dijkstra(vertice_inicial - 1)
            path = grafo.reconstruir_caminho(predecessores, vertice_inicial - 1, vertice_final - 1)
            print(f'Distância do vértice {vertice_inicial} ao vértice {vertice_final}: {distances[vertice_final - 1]}')
            print(f'Caminho mínimo do vértice {vertice_inicial} ao vértice {vertice_final}: {path}')
        else:
            # Para grafos sem pesos
            familia, niveis, predecessores = grafo.bfs(vertice_inicial)
            print(f'Distância do vértice {vertice_inicial} ao vértice {vertice_final}: {niveis.get(vertice_final - 1, "Inacessível")}')
            path = grafo.reconstruir_caminho(predecessores, vertice_inicial - 1, vertice_final - 1)
            print(f'Caminho mínimo do vértice {vertice_inicial} ao vértice {vertice_final}: {path}')


print('\n-=-=-=-=-=-=-=-= FIM =-=-=-=-=-=-=-=-=\n')


# familia, niveis, predecessores = grafo.bfs(4)
# print('familia: ', familia)
# print(f'niveis: {niveis}')
# print(f'predecessores: {predecessores}')