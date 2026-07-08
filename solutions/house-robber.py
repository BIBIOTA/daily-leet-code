from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # Examples:
        # Input: nums = [1, 2, 3, 1]  → Output: 4
        # Input: nums = [2, 7, 9, 3, 1] → Output: 12
        if len(nums) == 0:
            return 0
    
        prev_2 = 0
        prev_1 = 0
        for i in range(0, len(nums)):
            current = max(prev_2 + nums[i], prev_1)
            prev_2 = prev_1
            prev_1 = current
        return max(prev_2, prev_1)