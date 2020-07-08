class Stack():
    def __init__(self, size):
        self.lista = []
        self.size = size

    def push(self, val):
        if not self.is_full():
            self.lista.append(val)
        else:
            print(f"Pilha Cheia")

    def pop(self):
        if not self.is_empty():
            self.lista.pop()
        else:
            print(f"Pilha Vazia")

    def is_empty(self):
        return len(self.lista) == 0

    def is_full(self):
        return len(self.lista) == self.size

    def __str__(self):
        return str(f"Pilha: {self.lista}")


p = Stack(4)
p.push(1)
p.push(2)
p.push(3)
p.push(4)
p.push(5)
p.pop()
p.pop()

print(p)
