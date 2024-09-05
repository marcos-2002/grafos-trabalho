from collections import defaultdict

class Grafo:
    def __init__(self, tamanho, arestas):
        self.tamanho = tamanho
        self.arestas = arestas
        self.m_adjacencia = defaultdict(list)
        self.l_adjacencia = defaultdict(list)
        self.matriz_adjacencia()
        self.lista_adjacencia()

    def getTamanho(self):
        return self.tamanho
    
    def getAresta(self):
        return self.arestas
    
    def getM_adjacencia(self):
        return self.m_adjacencia
    
    def getL_adjacencia(self):
        return self.l_adjacencia
    
    def matriz_adjacencia(self):
        lis = []
        for x in range(self.tamanho):
            lis.append(0)
        for x in range(self.tamanho):
            self.m_adjacencia[x] = lis.copy()
        for aresta in self.arestas:
            self.m_adjacencia[aresta[0] - 1][aresta[1] - 1] = 1
            self.m_adjacencia[aresta[1] - 1][aresta[0] - 1] = 1
    
    def lista_adjacencia(self):
        lis = []
        for elemento in self.m_adjacencia:
            cont = 0
            for valor in self.m_adjacencia[elemento]:
                if(valor == 1):
                    lis.append(cont)
                cont += 1
            self.l_adjacencia[elemento] = lis.copy()
            lis.clear()
    
    def bfs(self, inicio):
        inicio = inicio - 1
        pilha = list()
        visitados = list()
        pilha.append(inicio)
        visitados.append(inicio)
        familia = defaultdict(list)
        while len(pilha) > 0:
            pai = self.m_adjacencia[pilha[0]]
            nome_pai = pilha[0]
            del pilha[0]
            for x in range(len(pai)):
                if (pai[x] == 1) and (x not in visitados):
                    visitados.append(x)         # acabou de visitar um novo nó
                    pilha.append(x)             # coloca o nó na pilha pra visitar os filhos dele
                    familia[nome_pai + 1].append(x + 1) # adiciona o nó pai e seus filhos
        return familia

    def dfs(self, inicio):
        inicio = inicio - 1
        pilha = [inicio]
        visitados = {i: 'branco' for i in range(len(self.m_adjacencia))} # começa com todos brancos

        while pilha:
            vertice_atual = pilha.pop()
            for x in reversed(range(len(self.m_adjacencia[vertice_atual]))):
                if self.m_adjacencia[vertice_atual][x] == 1 and visitados[x] == 'branco':
                    pilha.append(x)             # adiciona o vertive ainda não visitado na lista
            visitados[vertice_atual] = 'verde'  # como o vertice foi completamente visitado ele é marcado como verde
            print('Visitados: ', visitados)
        return visitados
    
    
