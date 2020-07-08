# Vetor não tem um desempenho bom para realizar edição na lista

class No():

    
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class ListaEncadeada():


    def __init__(self):
        self._inicio = None
        self._quantidade = 0

    @property
    def inicio(self):
        return self._inicio

    @property
    def quantidade(self):
        return self._quantidade

    def _celula(self, posicao):
        self._validar_posicao(posicao)
        atual = self.inicio
        for i in range(0, posicao):
            atual = atual.proximo
        return atual

    def _validar_posicao(self, posicao):
        if 0 <= posicao and posicao < self._quantidade:
            return True
        raise IndexError(f'Posição inválida {posicao}')

    def inserir_inicio(self, valor):
        celula = No(valor)
        celula.proximo = self._inicio
        self._inicio = celula
        self._quantidade += 1
    
    def inserir(self, posicao, valor):
        if posicao == 0:
            self.inserir_inicio(valor)
        else:
            celula = No(valor)
            esquerda = self._celula(posicao-1)
            celula.proximo = esquerda.proximo
            esquerda.proximo = celula
            self._quantidade += 1

    def imprimir(self):
        atual = self.inicio
        valor = ''
        for i in range(0, self.quantidade):
            # print(atual.valor)
            valor = f'{valor} -> {atual.valor}'
            atual = atual.proximo
        print(valor)

    def remover_inicio(self):
        removido = self.inicio
        self._inicio = removido.proximo
        removido.proximo = None
        self._quantidade -= 1
        return removido.valor

    def remover(self, posicao):
        esquerda = self._celula(posicao-1)
        removido = esquerda.proximo
        esquerda.proximo = removido.proximo
        removido.proximo = None
        self._quantidade -= 1
        return removido.valor

    def item(self, posicao):
        self._validar_posicao(posicao)
        celula = self._celula(posicao)
        return celula.valor