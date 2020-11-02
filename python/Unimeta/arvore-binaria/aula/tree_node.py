class TNode:
    # Intancia os nós da arvore
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f'{self.value}'


class BinTree:
    # instancia a arvore
    def __init__(self, value=None):
        if value: # Se value != None
            node = TNode(value)
            self.root = node    # Define raiz da árvore
        self.root = None # Se value == None
    
    def pos_order(self, node=None):
        # Navega em pós ordem
        if node is None:
            node = self.root
        if node.left:
            self.pos_order(node.left)
        if node.right:
            self.pos_order(node.right)
        print(f'{node}', end='')

if __name__ == '__main__':
    arvore = BinTree()

    n1 = TNode('A')
    n2 = TNode('C')
    n3 = TNode('P')
    n4 = TNode('K')
    n5 = TNode('O')
    n6 = TNode('F')
    n7 = TNode('E')
    n8 = TNode('B')
    n9 = TNode('I')
    n10 = TNode('U')

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n4.right = n7
    n7.left = n10
    n3.right = n6
    n6.left = n8
    n6.right = n9

    arvore.root = n1

    arvore.pos_order()
