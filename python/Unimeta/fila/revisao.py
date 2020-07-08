class Stack():

    def __init__(self, size):
        self.lista = []
        self.size = size

    def equeue(self, a):
        if len(self.lista) < self.size: # Testa se o tamanho da lista é menor que o tamanho máximo
            self.lista.append(a) # Empilha o dado passado pelo parâmetro "a"
        else:
            print("Erro. Fila já está cheia.")

    def dqueue(self):
        if not self.is_empty(): # Testa se a lista não está vazia
            self.lista.pop(0)   # Remove o item na posição 0 (primeiro item da lista)
        else:
            print("Erro. Fila está vazia")
    
    def is_empty(self):
        return len(self.lista) == 0 # Retorna se o tamanho da lista é igual a 0 (True ou False)

    def __str__(self):
        return str(f"{self.lista}") # Restorna uma string com os dados da lista


x = Stack(3) # Instancia o objeto (tamanho máximo)

x.equeue("A")   # Empilha dado na fila
x.equeue("B")
x.dqueue()      # Desempilha o primeiro dado

print(x)        # Imprime o objeto
