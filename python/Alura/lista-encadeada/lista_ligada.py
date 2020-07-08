class Celula:

    def __init__(self, conteudo):
        self.conteudo = conteudo
        self.proximo = None


class ListaLigada:
    
    def __init__(self):
        self._inicio = None
        self._quantidade = 0

    @property
    def inicio(self):
        return self._inicio

    @property
    def quantidade(self):
        return self._quantidade

    def inserir_inicio(self, conteudo):
        celula = Celula(conteudo)
        celula.proximo = self._inicio
        self._inicio = celula
        self._quantidade += 1

    def inserir(self, posicao, conteudo):
        if posicao == 0:
            self.inserir_inicio(conteudo)
            return
        celula = Celula(conteudo)
        esquerda = self._celula(posicao-1)
        celula.proximo = esquerda.proximo
        esquerda.proximo = celula
        self._quantidade += 1

    def _celula(self, posicao):
        self._validar_posicao(posicao)
        atual = self.inicio
        for i in range(0, posicao):
            atual = atual.proximo
        return atual

    def _validar_posicao(self, posicao):
        if 0 <= posicao < self.quantidade:
            return True
        raise IndexError(f"Posição Inválida {posicao}")

    def imprimir(self):
        atual = self.inicio
        for i in range(0, self.quantidade):
            print(atual.conteudo)
            atual = atual.proximo

    def remover_inicio(self):
        removido = self.inicio
        self._inicio = removido.proximo
        removido.proximo = None
        self._quantidade -= 1
        return removido.conteudo

    def remover(self, posicao):
        if posicao == 0:
            return self.remover_inicio
        esquerda = self._celula(posicao - 1)
        removido = esquerda.proximo
        esquerda.proximo = removido.proximo
        removido.proximo = None
        self._quantidade -= 1
        return removido.conteudo

    def item(self, posicao):
        self._validar_posicao(posicao)
        celula = self._celula(posicao)
        return celula.conteudo