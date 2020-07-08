class Pilha:
    def __init__(self):
        self.items = []
    def empilhar(self, item):
        self.items.append(item)
    def desempilhar(self):
        if self.isEmpty():
            return False
        else:
            return self.items.pop()
    def isEmpty(self):
        return (self.items == [])

entrada = "(((((((a+b))))))a+c)"
saida = ""
operadores = ['-','+','/','*','^']
pilha = Pilha()
for i in entrada:
    #verifica se o item é um parentese de abertura
    if i == '(':
        pilha.empilhar(i)
    # verifica se o item é um parentese de fechamento
    elif i== ')':
        # verifica se a pilha esta vazia
        if not pilha.isEmpty():
            desempilha = ''
            #enquanto a não encontra o parentese de fechamento ele desempilha
            while  desempilha != '(':

                desempilha = pilha.desempilhar()
                if desempilha not in ['(',')']:
                    saida = saida + desempilha
                elif not desempilha:
                    print('A expressão de entrada não é válida')
                    break

        # verifica se o item é um parentese de abertura
        else:
            print('A expressão de entrada não é válida')
    #verifiacr se é um operador
    elif i in operadores:
        p = pilha.desempilhar()
        if p:
            pilha.empilhar(p)
        if pilha.isEmpty():
            pilha.empilhar(i)

        elif p == '(':
            pilha.empilhar(i)

        else:

            desempilhado = pilha.desempilhar()

            if operadores.index(i)> operadores.index(desempilhado):
                pilha.empilhar(desempilhado)
                pilha.empilhar(i)
            elif operadores.index(i)== operadores.index(desempilhado):
                saida = saida+desempilhado
                pilha.empilhar(i)
            else:
                while operadores.index(i)< operadores.index(desempilhado):
                    saida = saida + desempilhado
                    desempilhado = pilha.desempilhar()
                    if not desempilhado:
                        break

                pilha.empilhar(i)
    #coloca o  na string de saída
    else:
        saida=saida+i
desempilha = pilha.desempilhar()
while desempilha:
    saida = saida+desempilha
    desempilha = pilha.desempilhar()
print(saida)