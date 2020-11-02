class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def __repr__(self):
        return str(self.value)


class BinaryTree:
    def __init__(self, value=None):
        if value:
            node = Node(value)
            self.root = node
        else:
            self.root = None
            
    def width_search(self):
        width = [self.root]
        while len(width) > 0:
            aux = []
            for item in width:
                print([item.value], end=' ')
                if item.left:
                    aux.append(item.left)
                if item.right:
                    aux.append(item.right)
            width = aux
            print('')


if __name__ == '__main__':
    tree = BinaryTree()
    
    a = Node('A')
    b = Node('B')
    c = Node('C')
    d = Node('D')
    e = Node('E')
    f = Node('F')
    g = Node('G')
    h = Node('H')
    i = Node('I')
    
    tree.root = e
    
    e.left = d
    e.right = f
    d.left = c
    f.right = g
    c.left = b
    g.right = h
    b.left = a
    h.right = i
    
    print('\nbusca_em_largura:')
    tree.width_search()
