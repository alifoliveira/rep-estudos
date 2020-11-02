from node import Node
from binary_tree import BinaryTree

if __name__ == '__main__':
    tree = BinaryTree()
    
    A = Node('A')
    B = Node('B')
    C = Node('C')
    D = Node('D')
    E = Node('E')
    F = Node('F')
    G = Node('G')
    
    tree.root = D
    
    D.left = C
    C.left = A
    C.right = B
    D.right = E
    E.left = F
    E.right = G
    
    tree.in_order()
    print('')
    
    tree.pre_order()
    print('')
    
    tree.pos_order()
    print('')
    
    tree.width_search()
    print('')
    