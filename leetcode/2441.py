"""
Find the largest positive integer k such that -k also exists in the array
If k don't exists, return -1
"""

class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        k = -1
        negatives = set()
        
        for num in nums:
            if num < 0:
                negatives.add(num)
            
        for num in nums:
            if -num in negatives:
                k = max(k, num)
                
        return k
        
        # nums.sort()
        # neg, pos = 0, len(nums) -1
        
        # while neg < pos:
        #     if -nums[neg] == nums[pos]:
        #         return nums[pos]
        #     elif -nums[neg] > nums[pos]:
        #         neg += 1
        #     else: 
        #         pos -=1
            
        # return -1
        