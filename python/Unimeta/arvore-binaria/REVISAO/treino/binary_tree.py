from node import Node

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
                
