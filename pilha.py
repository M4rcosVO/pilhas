class Pilha:
    def __init__(self):
        self.itens = []  # FPVazia()

    def PEhVazia(self):
        return len(self.itens) == 0

    def PEmpilha(self, item):
        self.itens.append(item)

    def PDesempilha(self):
        if self.PEhVazia():
            raise Exception("Erro: Pilha vazia.")
        return self.itens.pop()

    def PTamanho(self):
        return len(self.itens)


# Exemplo de uso
if __name__ == "__main__":
    p = Pilha()

    # FPVazia() já é feito no __init__
    p.PEmpilha(10)
    p.PEmpilha(20)
    p.PEmpilha(30)

    print("Tamanho da pilha:", p.PTamanho())

    while not p.PEhVazia():
        print("Elemento removido:", p.PDesempilha())
