from lista_ligada import ListaLigada, Celula

class Loja:

    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def __repr__(self):
        return f'{self.nome}\n  {self.endereco}'


def main():
    loja1 = Loja("Mercadinho", "Rua das Laranjeiras, 12")
    loja2 = Loja("Hortifruti", "Rua do Pomar, 300")
    loja3 = Loja("Padaria", "Rua das Flores, 671")
    loja4 = Loja("Supermercado", "Alameda Santos, 524")
    loja5 = Loja("Mini mercado", "Rua da Fazenda, 900")
    loja6 = Loja("Quitanda", "Avenida Rio branco, 34")

    lista = ListaLigada()
    lista.inserir_inicio(loja1)
    lista.inserir_inicio(loja2)
    lista.inserir_inicio(loja3)
    lista.inserir(1, loja4)
    lista.inserir(0, loja5)
    lista.inserir(lista.quantidade, loja6)

    print(f'Quantidade: {lista.quantidade}')
    lista.imprimir()
    removido = lista.remover_inicio()
    print(f'Removido: {removido}')
    print(f'Quantidade: {lista.quantidade}')
    removido = lista.remover_inicio()
    print(f'Removido: {removido}')
    print(f'Quantidade: {lista.quantidade}')
    removido = lista.remover(2)
    print(f'Removido: {removido}')
    print(f'lista 0: {lista.item(0)}')

main()
