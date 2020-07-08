from node import Node

class Linked_List:
    def __init__(self):
        self.head = None

    def add_element(self, element):
        if self.head: # Already have elements
            pointer = self.head
            ancestor = pointer
            while (pointer.next): # pointer.next != None
                ancestor = pointer
                pointer = pointer.next
            # if there's no next element
            pointer.previous = ancestor # hey pointer, you acestor is me
            pointer.next = Node(element)
            new = pointer.next
            new.previous = pointer
        else: # Have no elements
            self.head = Node(element)
    
    def __repr__(self):
        l = ''
        pointer = self.head
        while(pointer):
            print(f'pointer: {pointer.value}')
            l += str(pointer.value) + ' → '
            pointer = pointer.next
            if not pointer:
                l += str('None')
        return l

    def __str__(self):
        return self.__repr__()


if __name__ == '__main__':
    lista = Linked_List()
    lista.add_element(5)
    lista.add_element(7)
    lista.add_element(8)
    lista.add_element(2)
    print(lista)
