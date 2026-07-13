from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Examples:
        # Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  → Output: 6   (subarray [4,-1,2,1])
        # Input: nums = [1]                                → Output: 1
        # Input: nums = [5, 4, -1, 7, 8]                  → Output: 23  (entire array)
        max_sum = current_sum = nums[0]
        for num in nums[1:]:
            current_sum = max(current_sum + num, num)
            max_sum = max(current_sum, max_sum)
        return max_sum