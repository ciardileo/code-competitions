"""

"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for num in range(len(nums)):
            try:
                complement = target - (nums[num]) if target > 0 and nums[num] < 0 else target - nums[num]
                complement = nums.index(complement)
                if complement != num:
                    return (num, complement)
            except:
                pass

    
numbers = [int(x) for x in input().split()]
target_number = int(input())

print(Solution.twoSum(None, numbers, target_number))

# optimized solution:
# def twoSum(self, nums: List[int], target: int) -> List[int]:
#     hashmap = {}
#     for i in range(len(nums)):
#         complement = target - nums[i]
#         if complement in hashmap:
#             return [i, hashmap[complement]]
#         hashmap[nums[i]] = i