from grafo import Grafo
from arquivo import *

tamanho, arestas = ler_arquivo()
grafo = Grafo(tamanho, arestas)
print("Tamanho: ", grafo.getTamanho())
print("Arestas: ", grafo.getAresta())
print("Matriz de adjacencia: ", grafo.getM_adjacencia())
print("Lista de adjacencia: ", grafo.getL_adjacencia())
print("\n")
for x in grafo.m_adjacencia:
    print(grafo.m_adjacencia[x])

print("\n-=-=-=-=-=-=-=-= componentes -=-=-=-=-=-==-=")
inicio = int(input('Digite o inicio: '))
familia, nivel = grafo.bfs(inicio)
print(f'Familia:', familia)
print(f'Nível de cada vértice: ', nivel)