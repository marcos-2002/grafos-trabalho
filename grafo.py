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