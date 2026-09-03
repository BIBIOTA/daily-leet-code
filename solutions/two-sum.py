from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in result:
                return [result[diff], i]
            result[nums[i]] = i


# Examples:
# Input: nums = [2, 7, 11, 15], target = 9  → Output: [0, 1]
# Input: nums = [3, 2, 4],      target = 6  → Output: [1, 2]
# Input: nums = [3, 3],         target = 6  → Output: [0, 1]
