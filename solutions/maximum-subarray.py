from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Examples:
        # Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  → Output: 6   (子陣列 [4,-1,2,1])
        # Input: nums = [1]                                 → Output: 1
        # Input: nums = [5, 4, -1, 7, 8]                   → Output: 23  (子陣列 [5,4,-1,7,8])
        current = nums[0]
        max_sum = nums[0]
        for num in nums[1:]:
            current += num
            if current < num:
                current = num
            if max_sum < current:
                max_sum = current
        return max_sum