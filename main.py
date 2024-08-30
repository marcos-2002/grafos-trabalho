def adjacenty(size, arestas):
   adjacenty_list = []
   lis = []
   for x in range(int(size)):
       lis.append(0)
   for x in range(int(size)):
       adjacenty_list.append(lis.copy())
   for aresta in arestas:
       adjacenty_list[int(aresta[0])-1][int(aresta[1])-1] = 1
       adjacenty_list[int(aresta[1])-1][int(aresta[0])-1] = 1
   return adjacenty_list 

def read():
    arestas = []
    cont = 0
    with open('entrada.txt', 'r') as inp:
        for line in inp:
            if(cont == 0):
                size = line.strip()
                cont += 1
                continue
            arestas.append(line.strip().split())
    return size, arestas

size, arestas = read()
adjacenty_list = adjacenty(size, arestas)
for x in adjacenty_list:
    print(x)