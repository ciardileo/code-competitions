"""
exemplo de uso de busca binária, nesse caso, quando o left passa o right, quer dizer que achamos o primeiro número que é menor do que estamos procurando, logo, devemos posicionar logo após ele (left + 1)
"""

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) -1
        
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                return middle
            
        return left
            