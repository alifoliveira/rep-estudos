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
        self.dell = 0
        if self.is_empty():
            raise ValueError('A pilha está vazia')
        else:
            self.dell += 1
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
        return str(f'Pilha: {self.lista}\nTamanho: {self.stack_size()}\nDeletados: {self.dell}')
  
size = 15
c = 0
pilha = Stack(size)

input_list = []
for i in range(size):
    input_list.append(int(input(f'{c+1}º Número: ')))
    c += 1

for n in input_list:
    if n%2 == 0:
        # Par
        pilha.push(n)
    else:
        # ìmpar
        pilha.pop()

print(f'\n{pilha}')
