class Stack():

    def __init__(self, size):
        self.lista = []
        self.size = size

    def push(self, a):
        if len(self.lista) < self.size: # Testa se a pilha não está cheia
            self.lista.append(a)
        else:
            print("Erro. A pilha já está cheia")

    def pop(self):
        if not self.is_empty(): # Testa se a lista não está vazia
            self.lista.pop()
        else:
            print("Erro. A pilha está vazia")

    def is_empty(self):
        return len(self.lista) == 0 # Testa te o tamanho da pilha é igual a 0 e retorna True ou False

    def __str__(self):
        return str(f"{self.lista}") # Retorna uma string com os dados da pilha


x = Stack(3) # O parâmetro é o tamanho máximo da pilha

x.push("A") # push = empilhar
x.push("B")
x.pop()     # pop = desempilhar

print(x)    # Imprime o Objeto
