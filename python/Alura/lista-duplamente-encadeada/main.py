from lista_encadeada import Node, ListaDuplamenteLigada

class Loja:
    
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def __repr__(self):
        return f'• {self.nome} - {self.endereco}'

def main():
    loja1 = Loja("Minimercado", "Rua das flores, 12")
    loja2 = Loja("Ortifrute", "Avenida das Borboletas, 23")
    loja3 = Loja("Padaria Pão Quentinho", "Praça da Árvore, 612")

    lista = ListaDuplamenteLigada()
    lista.inserir_inicio(loja1)
    lista.inserir_inicio(loja2)
    lista.inserir_inicio(loja3)

    # for i in range(lista.quantidade):
    #     print(f'# id: {i}')
    #     print(lista.item(i))
    # print(f'Quantidade: {lista.quantidade}')

    lista.imprimir()

main()
