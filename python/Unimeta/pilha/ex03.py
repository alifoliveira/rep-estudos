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
        return str(f'{self.lista}')

size = 15
s1 = Stack(size)
s2 = Stack(size)
aux = Stack(size)
input_list = []
c = 0

for n in range(size):
    input_list.append(int(input(f'{c+1}º Número: ')))
    c += 1
   
for i in input_list:
    # Insere na pilha "s1"
    s1.push(i)
print(f'Pilha 1: {s1}')

for j in range(size):
    # Trasfere da pilha "si" para pilha "aux"
    aux.push(s1.pop())

for k in range(size):
    # Trasnfere da pilha "aux" para pilha "s2"
    s2.push(aux.pop())
    
print(f'Pilha 2: {s2}')
