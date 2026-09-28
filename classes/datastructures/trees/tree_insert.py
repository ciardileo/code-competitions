def main():
    class Node:
        __slots__ = ("cur", "esq", "dir")
        def __init__(self, cur):
            self.cur = cur
            self.esq = None
            self.dir = None

    def inserir(raiz, valor):
        if raiz is None:
            return Node(valor)

        if valor > raiz.cur:
            # vai para a direita
            raiz.dir = inserir(raiz.dir, valor)
        else:
            raiz.esq = inserir(raiz.esq, valor)

        return raiz


    nodes = [10, 2, 3, 1, 18, 22, 37, 12, 11, 9]
    raiz = None
    for node in nodes:
        raiz = inserir(raiz, node)

    result = []
    def pre(raiz):
        if raiz is None:
            return

        result.append(raiz.cur)
        pre(raiz.esq)
        pre(raiz.dir)

    pre(raiz)
    print(result)


        
if __name__ == "__main__":
    main()