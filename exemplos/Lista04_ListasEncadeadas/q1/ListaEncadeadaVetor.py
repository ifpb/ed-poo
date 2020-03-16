'''
Construa a estrutura de lista encadeada básica utilizando as seguintes abordagens em Python:
- (i) representação encadeada como array
	*Tratar casos em que não seja possível adicionar ou remover um item.
'''

class ListaEncadeada:
    def __init__(self):
        self.nos = []

    def imprimir(self):
        for no in self.nos:
            print(no, end=" ")

    def adicionar(self, posicao, item):
        self.nos.insert(posicao, item)

    def remover(self, item):
        self.nos.remove(item)

    def procurar(self, item):
        return item in self.nos

    def atualizar(self, item, valor):
        for i in range(len(self.nos)):
            if item == self.nos[i]:
                self.nos[i] = valor

# lista = ListaEncadeada()
# lista.adicionar(0, 10)
# lista.adicionar(1, 30)
# lista.adicionar(2, 50)
# lista.remover(30)
# lista.atualizar(10, 100)
# lista.imprimir()