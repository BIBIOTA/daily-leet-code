from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Examples:
        # Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  → Output: 6  (subarray [4, -1, 2, 1])
        # Input: nums = [1]                                 → Output: 1
        # Input: nums = [5, 4, -1, 7, 8]                   → Output: 23 (entire array)
        current = num[0]
        best = num[0]
        for num in nums[1:]:
            if current + num < num:
                current = num
            else:
                current = current + num
            if current > best:
                best = current
        return best
