from linked_list import Node, Linked_List

class Create:

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'{self.value}'

def main():
    node1 = Create('Pêra')
    node2 = Create('Uva')
    node3 = Create('Maçã')
    node4 = Create('Abacaxi')
    node5 = Create('Laranja')
    node6 = Create('Morango')

    lista = Linked_List()
    lista.insert(node1, 0)
    lista.insert(node2, 1)
    lista.insert(node3, 2)
    lista.insert(node4, 3)
    lista.insert(node5, 4)
    lista.insert(node6, 1)
    lista.remove(0)
    
    lista.show()

main()
