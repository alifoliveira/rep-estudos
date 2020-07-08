# Lista encadeada
class No:
  def __init__(self, valor):
    self.valor = valor
    self.proximo = None


class ListaEncadeada:
  def __init__(self):
    self.cabeca = None

  # Adicionar nó ao final da lista
  def adicionarFinal(self, elemento):
    if self.cabeca: # quando já possui elementos
      ponteiro = self.cabeca
      while ponteiro.proximo:
        ponteiro = ponteiro.proximo
      ponteiro.proximo = No(elemento)
    else: # quando não possui elementos
      self.cabeca = No(elemento)
  
  # Adicionar nó na posição informada (indice)
  def inserirNo(self, indice, newValue):
    newNo = No(newValue)
    if self.cabeca:
      antecessor = None
      ponteiro = self.cabeca
      for i in range(indice):
        antecessor = ponteiro
        ponteiro = ponteiro.proximo
      antecessor.proximo = newNo
      newNo.proximo = ponteiro
    else:
      raise Exception("Lista Vazia")
  
  # Remover nó pelo indice informado
  def removerNo(self, indice):
    if self.cabeca:
      antecessor = None
      ponteiro = self.cabeca
      for i in range(indice):
        antecessor = ponteiro
        ponteiro = ponteiro.proximo
      antecessor.proximo = ponteiro.proximo
    else:
      raise Exception("Lista Vazia")

  # Exibir nó na posição informada
  def __getitem__(self, indice):
    ponteiro = self.cabeca
    for i in range(indice):
      if ponteiro:
        ponteiro = ponteiro.proximo
      else:
        raise IndexError("O indice informado não está na lista ou é nulo")
    if ponteiro:
      return f'[{ponteiro.valor}->{ponteiro.proximo.valor}]'
    else:
      raise IndexError("O índice informado não está na lista ou é nulo")
  
  # Editar Nó pelo indice informado
  def __setitem__(self, indice, newValue):
    ponteiro = self.cabeca
    for i in range(indice):
      if ponteiro:
        ponteiro = ponteiro.proximo
      else:
        raise IndexError("O indice informado não está na lista ou é nulo")
    if ponteiro:
      ponteiro.valor = newValue
    else:
      raise IndexError("O índice informado não está na lista ou é nulo")
      
  def __repr__(self):
    l = ''
    ponteiro = self.cabeca
    while ponteiro:
      l = l + str(ponteiro.valor) + '->'
      ponteiro = ponteiro.proximo
    return l
  
  def __str__(self):
    return self.__repr__()

  
if __name__ == '__main__':
  lista = ListaEncadeada()
  # Adicionar no final
  lista.adicionarFinal(1)
  lista.adicionarFinal(2)
  lista.adicionarFinal(3)
  lista.adicionarFinal(4)
  lista.adicionarFinal(5)
  lista.adicionarFinal(6) # Saida 1->2->3->4->5->6->

  # Editar nó pelo indice informado
  lista[2] = 10 # Saida 1->2->10->4->5->6->

  # Remover nó pelo indice informado
  lista.removerNo(2) # Saída 1->2->4->5->6->

  # Adicionar nó no indice informado
  lista.inserirNo(2, 3) # Saida 1->2->3->4->5->6->

  # Exibir nó pelo indice informado
  print(lista[3]) # Saida [4->5]


  print(lista)