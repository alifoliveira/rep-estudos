#map(funcao, *sequencia de args) --> Object map

def qua(x): return x**2

mapa = map(qua, [1, 2, 3, 4, 5])

listmap = list(map(qua, [1, 2, 3, 4, 5]))

ran = tuple(map(qua, range(10)))

lamb = list(map(lambda x: x**3, range(10)))

print(f'''
map(...) = {mapa}\n
list(map(...)) = {listmap}\n
tuple(map(..., range(10))) = {ran}\n
map(funcao lambda, ...) = {lamb}\n
      ''')

