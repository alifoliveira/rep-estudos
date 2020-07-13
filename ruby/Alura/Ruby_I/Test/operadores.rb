treze = 13
cinco = 5

# operadores
puts treze / cinco  # divisão
puts treze % cinco  # mod | resto da divisão
puts treze + cinco  # soma
puts treze - cinco  # subtração
puts treze * cinco  # multiplicação

# auto atribuição
numero = 5
numero += 1
numero -= 2
numero *= 2
numero /= 4
numero *= 13
numero %= 10
puts numero # 6

# sistema de tipos
quinze = "   quinze   "
puts quinze.strip

quinze = 15
puts quinze.strip # erro, quinze mudou o tipo para FixNum
