def ler_arquivo():
    arestas = []
    cont = 0
    with open('entrada.txt', 'r') as entrada:
        for linha in entrada:
            if(cont == 0):
                tamanho = int(linha.strip())
                cont += 1
                continue
            l = linha.strip().split()
            arestas.append([int(val) if i < 2 else float(val) for i, val in enumerate(l)])
    return tamanho, arestas