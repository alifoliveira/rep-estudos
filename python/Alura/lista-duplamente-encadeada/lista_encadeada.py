class Node:

    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None

class ListaDuplamenteLigada:

        def __init__(self):
            self._inicio = None
            self._fim = None
            self._quantidade = 0

        @property
        def inicio(self):
            return self._inicio

        @property
        def fim(self):
            return self._fim

        @property
        def quantidade(self):
            return self._quantidade

        def _inserir_lista_vazia(self, valor):
            node = Node(valor)
            self._inicio = node
            self._fim = None
            self._quantidade += 1

        def inserir_inicio(self, valor):
            if self.quantidade == 0:
                return self._inserir_lista_vazia(valor)
            node = Node(valor)
            node.proximo = self.inicio
            self._inicio.anterior = node
            self._inicio = node
            self._quantidade += 1

        def item(self, posicao): # Consulta Item da Lista
            node = self._node(posicao) # Envia consulta para tratamento em _node
            return node.valor # Retorna valor do item requisitado

        def _validar_posicao(self, posicao): # Verifica se posição existe na lista
            if 0 <= posicao < self.quantidade: 
                return True
            raise IndexError(f'Posição inválida {posicao}')

        def _node(self, posicao): # Verifica posição na lista
            self._validar_posicao(posicao) # Envia posição para validação em _validar_posicao
            atual = self.inicio
            for i in range(0, posicao): # Percorre lista procurando por posição requisitada
                atual = atual.proximo
            return atual # Retorna posição requisitada

        def imprimir(self):
            atual = self.inicio
            for i in range(self.quantidade):
                print(atual.valor)
                atual = atual.proximo
            



