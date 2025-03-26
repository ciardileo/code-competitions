"""
quantidade de combinações possíveis de preço para K produtos somando R
fazemos um backtracking que escolhe números crescentes, e caso a soma dos três números for igual a R, retornamos mais um ao count de combinações
"""


def main():
    valor, produtos = map(int, input().split())
    
    def backtrack(actual_sum, start, depth):
        """
        actual_sum = nossa soma atual
        start = numero que paramos a soma 
        depth = quantos números já temos
        """
        
        if depth == produtos:
            return 1 if actual_sum == valor else 0
        
        combinations = 0
        max_value_to_choose = valor - actual_sum - (produtos - depth - 1)
    
        for i in range(start, min(max_value_to_choose + 1, valor + 1)):
            if actual_sum + i > valor:
                break
            
            combinations += backtrack(actual_sum + i, i + 1, depth + 1)
            
        return combinations
    
    
    print(backtrack(0, 1, 0))

if __name__ == "__main__":
    main()

