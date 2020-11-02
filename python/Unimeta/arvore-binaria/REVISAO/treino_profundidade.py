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

    def in_order(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.in_order(node.left)
        print(node, end=' ')
        if node.right:
            self.in_order(node.right)
            
    def pre_order(self, node=None):
        if node is None:
            node = self.root
        print(node, end=' ')
        if node.left:
            self.pre_order(node.left)
        if node.right:
            self.pre_order(node.right)
            
    def pos_order(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.pos_order(node.left)
        if node.right:
            self.pos_order(node.right)
        print(node, end=' ')

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
    
    print('\n'+'em_ordem:')
    tree.in_order()

    print('\n'+'pre_ordem:')
    tree.pre_order()

    print('\n'+'pos_ordem:')
    tree.pos_order()
