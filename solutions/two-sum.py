from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        results = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in results:
                return [results[diff], i]
            results[num] = i


# Examples:
# twoSum([2, 7, 11, 15], 9)  -> [0, 1]  (2 + 7 = 9)
# twoSum([3, 2, 4], 6)       -> [1, 2]  (2 + 4 = 6)
# twoSum([3, 3], 6)           -> [0, 1]  (3 + 3 = 6)
