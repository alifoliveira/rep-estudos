class Stack():
    def __init__(self, size):
        self.lista = []
        self.size = size
    
    def push(self, a):
        if len(self.lista) < self.size:
            return self.lista.append(a)
        else:
            raise ValueError('A pilha já está cheia')
    
    def pop(self):
        if self.is_empty():
            raise ValueError('A pilha está vazia')
        else:
            return self.lista.pop()
    
    def stack_size(self):
        count = 0
        for i in self.lista:
            if i:
                count += 1 # quantidade de slots preenchidos
        return f'{count}/{self.size}'
    
    def is_empty(self):
        return len(self.lista) == 0
    
    def __str__(self):
        return str(f'Pilha: {self.lista}\nTamanho: {self.stack_size()}')
  
# nome.push -> empilha elemento
# nome.pop -> desempilha elemento
# print(nome) -> mostra elementos empilhados e tamanho

pilha = Stack(5) # Stack(tamanho_max)

pilha.push('a') # name.push(elemento)
pilha.push('b')
pilha.push('c')
pilha.push('d')
pilha.pop()

print(pilha)
