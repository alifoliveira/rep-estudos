class Stack():
    def __init__(self):
        self.lista = []
    
    def push(self, a):
        self.lista.append(a)
    
    def pop(self):
        if self.isEmpty():
            print('Ação negada, a pilha está vazia')
        else:
            return self.lista.pop()
    
    def isEmpty(self):
        return len(self.lista) == 0

    def __str__(self):
        return str(self.lista)


pilha = Stack()
reversa = Stack()

input_data = input('\nDigite qualquer frase: ')
input_data = input_data.lower()

# Inverte a string lida

for i in input_data:
    pilha.push(i)

size = len(input_data)

for j in range(size):
    reversa.push(pilha.pop())

print(f'Reverso = {reversa}')

# Testa se a string lida é um palíndromo

for i in input_data:
    pilha.push(i)

test = True

for k in range(size):
    if test == False:
        break
    else:
        if pilha.pop() == reversa.pop():
            test = True
        else:
            test = False

if test:
    print(f'A string "{input_data}" é um palíndromo\n')
else:
    print(f'A string "{input_data}" não é um palíndromo\n')
