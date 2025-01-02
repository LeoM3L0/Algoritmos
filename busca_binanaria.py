def busca_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (alto + baixo) // 2 # No primeiro loop o valor de meio é 500.000 mil
        chute = lista[meio]        #chute sera maior que o item caso o item for por exemplo 10
        if chute == item:          # alto = 499.999 e meio passa a ser 250.000 
            return meio            # pq (alto = 500.000 e baixo = 0 e // 2 ficara 250.000) 
        if chute > item:           # E assim por diante até chegar em 10
            alto = meio - 1        # logo será log10000000 = 7 pq 10 elevado a 7 é = 10000000
        else:
            baixo = meio + 1
    return None

lista_numeros = list(range(1, 1000001))

item = int(input())

resultado =  busca_binaria(lista_numeros, item)

print(f"Item encontrado na posição {resultado}")