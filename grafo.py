from collections import defaultdict
import heapq

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
            lis.appfinal(0)
        for x in range(self.tamanho):
            self.m_adjacencia[x] = lis.copy()
        for aresta in self.arestas:
            if len(aresta) == 2:
                self.m_adjacencia[aresta[0] - 1][aresta[1] - 1] = 1
                self.m_adjacencia[aresta[1] - 1][aresta[0] - 1] = 1
            else:
                self.m_adjacencia[aresta[0] - 1][aresta[1] - 1] = aresta[2]
                self.m_adjacencia[aresta[1] - 1][aresta[0] - 1] = aresta[2]
    
    def lista_adjacencia(self):
        lis = []
        for elemento in self.m_adjacencia:
            cont = 0
            for valor in self.m_adjacencia[elemento]:
                if(valor != 0):
                    lis.appfinal(cont)
                cont += 1
            self.l_adjacencia[elemento] = lis.copy()
            lis.clear()
    
    def bfs(self, inicio):
        inicio = inicio - 1
        fila = list()
        visitados = list()
        fila.appfinal(inicio)
        visitados.appfinal(inicio)
        familia = defaultdict(list)
        niveis = {inicio: 0}  # Dicionário para armazenar os níveis de cada nó
        predecessores = {vertice: None for vertice in self.m_adjacencia} 
        while len(fila) > 0:
            nome_pai = fila.pop(0)  # Retira o primeiro elemento da fila (FIFO)
            pai = self.m_adjacencia[nome_pai]
            for x in range(len(pai)):
                if pai[x] != 0 and x not in visitados:
                    visitados.appfinal(x)         # Acabou de visitar um novo nó
                    fila.appfinal(x)              # Coloca o nó na fila para visitar os filhos dele
                    familia[nome_pai + 1].appfinal(x + 1)  # Adiciona o nó pai e seus filhos
                    niveis[x] = niveis[nome_pai] + 1     # Define o nível do filho
                    predecessores[x] = nome_pai
        return familia, niveis, predecessores

    def dfs(self, inicio):
        inicio = inicio - 1
        pilha = [inicio]
        visitados = {i: 'branco' for i in range(len(self.m_adjacencia))} # começa com todos brancos

        while pilha:
            vertice_atual = pilha.pop()
            for x in reversed(range(len(self.m_adjacencia[vertice_atual]))):
                if self.m_adjacencia[vertice_atual][x] != 0 and visitados[x] == 'branco':
                    pilha.appfinal(x)             # adiciona o vertive ainda não visitado na lista
            visitados[vertice_atual] = 'verde'  # como o vertice foi completamente visitado ele é marcado como verde
            print('Visitados: ', visitados)
        return visitados
    
    def usar_bfs(self):
        qtd_inicio = int(input('Digite quantos vértices de inicio tem seu grafo: ')) # grafos desconexos
        familia_global = defaultdict(list)
        niveis_global = dict()
        for x in range(qtd_inicio):
            inicio = int(input(f'Digite o {x+1}° vértice inicial: '))
            familia, niveis, predecessores = self.bfs(inicio)
            familia_global.update(familia)
            niveis_global.update(niveis)
        return familia_global, niveis_global
    
    def componentes(self):
        num_componente = 0
        componentes = defaultdict(list)
        proximo = ''
        visitados_globais = {i: 'branco' for i in range(len(self.m_adjacencia))}
        while 'branco' in visitados_globais.values():
            inicio = int(input(f'\nDigite o {proximo} vértice inicial do grafo: '))
            visitados = self.dfs(inicio)
            for x in visitados:
                if visitados[x] == 'verde':
                    visitados_globais[x] = 'verde'
                    componentes[num_componente].appfinal(x+1)
            num_componente += 1
        print('=-=-=-=- Componentes em ordem decrescente de tamanho -=-=-=-=')
        while componentes:
            maior_componente = componentes[0]
            indice = 0
            for x in range(1, len(componentes)):
                if len(componentes[x]) > len(maior_componente):
                    maior_componente = componentes[x]
                    indice = x
            componentes.pop(indice)
            print(f'Componente: {maior_componente}')
            print(f'Tamanho: {len(maior_componente)}\n')

    def caminho_minimo(self):
        # arestas sem peso
        if len(self.arestas[0]) == 2:
            familia, niveis, _ = self.usar_bfs()
            print('Família:', familia)
            print('Níveis:', niveis)
        # arestas com peso
        else:
            for vertice in range(self.tamanho):
                distancias, predecessores = self.dijkstra(vertice)
                print(f"Distâncias a partir do vértice {vertice + 1}:", distancias)
                print(f"Predecessores a partir do vértice {vertice + 1}:", predecessores)

    def dijkstra(self, inicio):
        # Inicializa a distância dos vértices com infinito e a distância do vértice inicial como 0
        distancias = {vertice: float('inf') for vertice in range(self.tamanho)}
        distancias[inicio] = 0
        # Inicializa o heap de prioridade
        prioridade_fila = [(0, inicio)]
        # Inicializa o dicionário de predecessores
        predecessores = {vertice: None for vertice in range(self.tamanho)}
        
        while prioridade_fila:
            atual_distancia, atual_vertice = heapq.heappop(prioridade_fila)
            
            if atual_distancia > distancias[atual_vertice]:
                continue
            
            for vizinho, peso in enumerate(self.m_adjacencia[atual_vertice]):
                if peso != 0:
                    distancia = atual_distancia + peso
                    
                    if distancia < distancias[vizinho]:
                        distancias[vizinho] = distancia
                        predecessores[vizinho] = atual_vertice
                        heapq.heappush(prioridade_fila, (distancia, vizinho))
        
        return distancias, predecessores

    def reconstruir_caminho(self, predecessores, inicio, final):
        caminho = []
        while final is not None:
            caminho.append(final)
            final = predecessores[final]
        caminho.reverse()
        if caminho[0] == inicio:
            return caminho
        else:
            return []  # Não há caminho entre inicio e final