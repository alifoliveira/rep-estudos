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
 
size = 6
c = 0
pos = Stack(size)
neg = Stack(size)
input_list = []

for n in range(size):
    input_list.append(int(input(f'{c+1}º Número: ')))
    c += 1

for i in input_list:
    if i > 0:
        # Positivo
        pos.push(i)
    elif i < 0:
        # Negativo
        neg.push(i)
    else:
        # Zero
        pos.pop()
        neg.pop()
        
print(f'Pilha Positiva: {pos}\nPilha Negativa: {neg}')