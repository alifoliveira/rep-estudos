# Essa classe cria os nós da lista
class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

# Essa classe faz as inserções e manipulações da lista
class Linked_List:

    def __init__(self):
        self._start = None # Inicio da lista [padrão = None]
        self._amount = 0

    @property # Possibilita chamar a funcão como propriedade [ex: initial_value = node.inicio]
    def start(self):
        return self._start

    @property
    def amount(self):
        return self._amount
    
    def insert(self, value, pos):
        if pos == 0:
            cell = Node(value)
            cell.next = self._start
            self._start = cell
            self._amount += 1
            return
        cell = Node(value)
        left_node = self._node(pos-1)
        cell.next = left_node.next
        left_node.next = cell
        self._amount += 1

    def _node(self, pos):
        self._position_check(pos)
        current = self.start
        for i in range(pos):
            current = current.next
        return current

    def _position_check(self, pos):
        # Verificar se a posição passada é válida
        if pos >= 0:
            return True
        raise IndexError('Posição inválida')

    def show(self):
        # Imprime os valores da lista em ordem 0 → n-1
        current = self.start
        for i in range(self.amount):
            print(f'{current.value}')
            current = current.next

    def remove(self, pos):
        # Remove elementos da lista (pela posição)
        if pos == 0:
            deleted = self.start
            self._start = deleted.next
            deleted.next = None
            self._amount -= 1
            return deleted.value
        left_node = self._node(pos - 1)
        deleted = left_node.next
        left_node.next = deleted.next
        deleted.next = None
        self._amount -= 1
        return deleted.value

    def edit(self, value, pos):
        self._position_check(pos)

    def item(self, pos):
        self._position_check(pos)
        cell = self._node(pos)
        return cell.value
