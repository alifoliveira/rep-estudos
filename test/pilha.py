# LIFO
livros = []
for livro in range(3):
    livros.append(f'Livro {livro+1}')

print(f'\n\nLivros: {livros}')
print(f'Removido: {livros.pop()}')
print(f'Livros: {livros}\n\n')