"""
para cada número no range, fazer uma busca binária para saber se ele está presente
no pior dos casos:
 O(log n^2)
"""

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums.sort()
        
        def bsearch(value: int) -> int:
            left = 0
            right = len(nums) - 1
            
            while left <= right:
                middle = (left + right) // 2
                if nums[middle] > value:
                    right = middle - 1
                elif nums[middle] < value:
                    left = middle + 1
                else:
                    return -1
                
            return value
        
        for i in range(len(nums) + 1):
            result = bsearch(i)
            if result != -1:
                return result
            
s = Solution()
print(s.missingNumber([3,0,1]))
                