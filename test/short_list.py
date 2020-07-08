# List comprehension 

# method 1 syntax:
# list = []
# for x in expression:
#    list.append(x)

# Method 2 syntax:
# list(map(function, sequence))
# list(map(lambda x: x*7, range(11)))

# method 3 syntax:
# [return for x in sequence]
# [x*7 for x in range(11)]

# Method 1
quadrados = []
for x in range(11):
    quadrados.append(x**2)

# Method 2
quadrado = list(map(lambda y: y**2, range(11)))

# Method 3
qua = [z**2 for z in range(11)]


print(f'Standard: {quadrados}')
print(f'Method 1: {quadrado}')
print(f'Method 2: {qua}')
