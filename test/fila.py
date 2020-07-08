# FIFO
from collections import deque

fila = deque([])
for livro in range(3):
    fila.append(f'Livro {livro+1}')
    
print(f'\n\nFila: {fila}')
print(f'Removido: {fila.popleft()}')
print(f'Fila: {fila}\n\n')
