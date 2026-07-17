from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Examples:
        # Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4] → Output: 6  (subarray: [4, -1, 2, 1])
        # Input: nums = [1]                               → Output: 1
        # Input: nums = [5, 4, -1, 7, 8]                → Output: 23 (subarray: [5, 4, -1, 7, 8])
        last_sum = max_sum = nums[0]
        for i in range(1, len(nums)):
            last_sum = max(last_sum + nums[i], nums[i])
            max_sum = max(last_sum, max_sum) 
        return max_sum