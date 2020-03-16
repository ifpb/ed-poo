class No:
    def __init__(self, carga, prox=None):
        self.carga = carga
        self.proximo = prox

    def __str__(self):
        return str(self.carga)

class ListaEncadeada:
    def __init__(self, cabeca=None):
        self.cabeca = cabeca

    def imprimir(self):
        atual = self.cabeca
        while atual is not None:
            print(atual)
            atual = atual.proximo

    def inserirNoInicio(self, no):
        if self.cabeca is None:
            self.cabeca = no
            return
        no.proximo = self.cabeca
        self.cabeca = no

    def inserirNoFim(self, no):
        if self.cabeca == None:
            self.cabeca = no
            return
        atual = self.cabeca
        while atual.proximo != None:
            atual = atual.proximo
        atual.proximo = no

    def procurarElemento(self, no):
        atual = self.cabeca
        while atual != None:
            if atual.carga == no.carga:
                return True
            atual = atual.proximo
        return False

    def remover_por_valor(self, no):
        atual = self.cabeca
        anterior = None
        if atual.proximo == None and atual.carga == no.carga:
            self.cabeca = None
        while atual != None:
            if no.carga == atual.carga:
                if anterior != None:
                    anterior.proximo = atual.proximo
                else:
                    self.cabeca = atual.proximo
            anterior = atual
            atual = atual.proximo

    def remover_por_indice(self, indice):
        contador = 0
        atual = self.cabeca
        anterior = None
        while atual != None:
            if indice == contador:
                if anterior != None:
                    anterior.proximo = atual.proximo
                else:
                    self.cabeca = atual.proximo
            anterior = atual
            atual = atual.proximo
            contador += 1

    def atualizar_carga(self, no, nova_carga):
        atual = self.cabeca
        while atual != None:
            if no.carga == atual.carga:
                atual.carga = nova_carga
            atual = atual.proximo

lista = ListaEncadeada(No(10))
lista.inserirNoInicio(No(50))
lista.inserirNoFim(No(100))
lista.inserirNoInicio(No(100))
lista.atualizar_carga(No(100), 999)
lista.imprimir()

# lista = ListaEncadeada(No(5))
# lista.inserirNoInicio(No(10))
# lista.inserirNoFim(No(500))
# lista.inserirNoFim(No(900))
# lista.inserirNoFim(No(1000))
# lista.imprimir()
# if lista.procurarElemento(No(10)):
#     print("Nó 10 encontrado")
# else:
#     print("Nó 10 não encontrado")