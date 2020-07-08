class Stack():
    
    def __init__(self):
        self.lista = []

    def push(self, a):
        self.lista.append(a)

    def pop(self):
        if self.isEmpty():
            print('A pilha está vazia')
        else:
            return self.lista.pop()

    def isEmpty(self):
        return len(self.lista) == 0

    def __str__(self):
        return f'{self.lista}'


pilha = Stack()
backup = Stack()
input_list = []
size = 5
count = 0
for i in range(size):
    input_list.append(int(input(f'{count+1}º Item: ')))
    count += 1

for j in input_list:
    pilha.push(j)

c = int(input(f'\nEscolha um dos items da lista a seguir para removê-lo:\n{pilha}\n\nItem: '))

count = 0
for k in range(size):
    test = pilha.pop()
    if test == c:
        break
    else:
        count += 1
        backup.push(test)

for l in range(count):
    pilha.push(backup.pop())


print(f'Pilha: {pilha}')
