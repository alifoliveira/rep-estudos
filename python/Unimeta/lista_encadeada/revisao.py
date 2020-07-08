class No():

    def __init__(self,valor,prox):
        self.valor = valor
        self.prox = prox

    def __str__(self):
        return str(f'({self.valor},{self.prox})')


class ListaEncadeada():

    def __init__(self):
        self.__primeiro = None
        self.__ultimo = None
        self.__maior = ''
        self.__menor = ''
        self.__count = 0        
        
    def primeiro(self):
        print(self.__primeiro)

    def ultimo(self):
        print(self.__ultimo)

    def mostrar_estrutura(self):
        print(f'{Cor.WARNING}Lista Encadeada: {self.__primeiro}{Cor.ENDC}')

    def mostrar_tamanho(self):
        print(f'{Cor.WARNING}Quantidade de Elementos: {self.__count}{Cor.ENDC}')

    def maior(self):
        print(f'{Cor.WARNING}Maior valor: {self.__maior}{Cor.ENDC}')

    def menor(self):
        print(f'{Cor.WARNING}Menor valor: {self.__menor}{Cor.ENDC}')

    def insere_inicio(self,valor):
        self.valor = valor
        self.__primeiro = No(self.valor, self.__primeiro)
        if self.__ultimo == None:
            self.__ultimo = self.__primeiro
        self.__count += 1
        if len(self.valor) > len(self.__maior):
            self.__maior = self.valor
        if len(self.__menor) == 0:
            self.__menor = self.valor
        elif len(self.valor) != 0 and len(self.valor) <= len(self.__menor):
            self.__menor = self.valor

    def insere_final(self,valor):
        self.valor = valor
        p = No(self.valor, None)
        if self.__primeiro == None:
            self.__primeiro = p
            self.__ultimo = p
        else:
            self.__ultimo.prox = p        
            self.__ultimo = p
        self.__count += 1
        if len(self.valor) > len(self.__maior):
            self.__maior = self.valor
        if len(self.__menor) == 0:
            self.__menor = self.valor
        elif len(self.valor) != 0 and len(self.valor) <= len(self.__menor):
            self.__menor = self.valor

    def remover_inicio(self):
        self.__primeiro = self.__primeiro.prox
        if self.__primeiro == None:
            self.__ultimo = None
        self.__count -= 1

    def remover_fim(self):
        if self.__primeiro.prox == None:
            self.__primeiro == None
        else:
            p = self.__primeiro
            while p.prox != self.__ultimo:
                p = p.prox
            p.prox = p.prox.prox
            if p.prox == None:
                self._ultimo = p
        self.__count -= 1


class Cor():
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


le = ListaEncadeada()
le.insere_inicio('encadeada')
le.insere_inicio('lista')
le.insere_inicio('parece que')
le.insere_final('funcionando')
le.insere_final('corretamente')
le.insere_final('certo?')
le.remover_inicio()
le.remover_fim()
le.mostrar_estrutura()
le.mostrar_tamanho()
le.maior()
le.menor()
