"""
cada roupa é identificada por um tipo e tamanho
tabela em q cada linha é um tipo, e cada coluna é um tamanho
cada celula é o estoque
a cada venda o estoque tem que ser atualizado, caso não tenha estoque, a venda não é efetuada
determine o número de vendas
M, N = número de tipos, número de tamanhos
"""

"""
criar uma matrix do estoque a partir do input
criar uma função de venda, recebendo linha, coluna e retornando 1 se a venda foi feita e 0 se não
A função vai incrementar a variável número de vendas
"""

def main():
    
    def pedido(estoque, tipo, tamanho):
        if estoque[tipo][tamanho] > 0:
            estoque[tipo][tamanho] -= 1
            return 1
        else:
            return 0
    
    estoque = []
    vendas = 0
    m, n = input().split()
    
    for _ in range(int(m)):
        linha = [int(x) for x in input().split()]
        estoque.append(linha)
        
    p = int(input())
    for _ in range(p):
        tipo, tamanho = input().split()
        vendas += pedido(estoque, int(tipo) - 1, int(tamanho) - 1)
        
    print(vendas)
        
    
if __name__ == "__main__":
    main()
    