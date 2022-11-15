def procura(lst,chave):
    for i in range(len(lst)):
        if lst[i] == chave:
            return i
    return -1
lista = [2,5,6,8]
key = int(input("valor a procurar na lista: "))

procura(lista, key)

