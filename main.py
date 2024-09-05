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

# print("\n-=-=-=-=-=-=-=-= bfs -=-=-=-=-=-==-=")
# inicio = int(input("Qual o vértice inicial: "))
# print(grafo.bfs(inicio))

print("\n-=-=-=-=-=-=-=-= dfs -=-=-=-=-=-==-=")
inicio = int(input("Qual o vértice inicial: "))
print(grafo.dfs(inicio))