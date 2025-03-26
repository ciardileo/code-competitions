"""
solved in 26/03/25
https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/description/
"""

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        """
        par + par = par
        par + ímpar = ímpar
        ímpar + ímpar = par

        isso implica que, se o x for diferente de 1 e não houverem apenas elementos ímpares, ou apenas elementos pares, não há nenhuma solução.
        o valor no qual todos devem se tranformar deve ser a mediana
        a diferença entre os outros números e a mediana deve ser divisível por X, ou seja, que conseguimos chegar de a (aleatório) à mediana por meio de adição e subtração do x.
        """
        
        if len(grid) == 1 and len(grid[0]) == 1:
            return 0
        
        sorted_list = []
        for i in grid:
            for j in i:
                sorted_list.append(j)

        sorted_list.sort()
        
        median = sorted_list[len(sorted_list) // 2]
        steps = 0
        
        for i in sorted_list:
            if abs(median - i) % x != 0:
                    return -1
                
            steps += abs(median - i) / x
            
        return int(steps)