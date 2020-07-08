class Fila():
    def __init__(self, tamanho):
        self.lista = []
        self.tam = tamanho

    def enqueue(self, item):
        if self.isFull():
            print("Erro, Lista Cheia")
        else:
            self.lista.append(item)

    def dequeue(self):
        if self.isEmpty():
            print("Erro, Lista Vazia")
        else:
            return self.lista.pop(0)

    def isEmpty(self):
        return len(self.lista) == 0

    def isFull(self):
        return len(self.lista) == self.tam

    def __str__(self):
        return f"{self.lista}"


size = 3
fila = Fila(size)
inverso = Fila(size)
aux = []
inv = []

for i in range(size):
    fila.enqueue(i+1)

print(f"Fila: {fila}")

for i in range(size):
    aux.append(fila.dequeue())
inv = [i for i in aux[::-1]]

for i in inv:
    inverso.enqueue(i)

print(f"Inverso: {inverso}")
