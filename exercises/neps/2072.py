"""
1. ler (em ordem): Número de dias, soma desejada, valores dos dias
2. armazenar os valores dos dias em um array 
3. criar um array de soma de prefixo (soma de todos os elementos até aquela posição)
4. percorro o array de soma de prefixo, e pra cada nova soma eu adiciono em um dicionário. Em todas as posições, se o valor da soma até a posição atual - valor desejado for igual a um valor que já exista no dicionário, quer dizer que ali existe um intervalo com a soma desejada
"""

def main():
    # variaveis
    valores = list()
    prefix_sum = list()
    qtd_somas = dict()
    resultado = 0
    
    # input
    dias = int(input())
    soma_desejada = int(input())
    valores = [int(x) for x in input().split()]
    
    # criacao do prefix sum array
    prefix_sum.append(0)
    for i in range(0, len(valores)):
        prefix_sum.append(prefix_sum[i] + valores[i])
    
    # fazendo a lógica para descobrir os intervalos com somas iguais, condições: o intervalo até ali é igual a S, ou alguma posição anteriormente registrada seja igual a atual - S, sendo assim, adicionar o número de vezes que essa soma estiver registrada
    for i in range(1, len(prefix_sum)):
        if prefix_sum[i] - soma_desejada in qtd_somas:
            resultado += qtd_somas[prefix_sum[i] - soma_desejada]
        
        qtd_somas[prefix_sum[i]] = qtd_somas.get(prefix_sum[i], 0) + 1
        
        if prefix_sum[i] == soma_desejada:
            resultado += 1
        
    print(resultado)
        
    
if __name__ == "__main__":
    main()