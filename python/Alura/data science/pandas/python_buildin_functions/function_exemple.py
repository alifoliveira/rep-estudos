def media_lista(lista):
    valor = sum(lista) / len(lista)
    return valor

def media_lista_qtd(lista):
    valor = sum(lista) / len(lista)
    return valor, len(lista)

resultado, quantidade = media_lista_qtd([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(resultado, quantidade)
