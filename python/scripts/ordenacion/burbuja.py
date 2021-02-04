# cerveza
def burbuja(lista):
    n = len(lista)
    if len(lista) <= 1:
        return lista
    else:
        for i in range(n-1):
            for j in range(n-i-1):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]

pato = [5, 7, 1, 9, 0, 4, 6, 2, 3, 8]
