from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Examples:
        # Input: nums = [1, 12, -5, -6, 50, 3], k = 4
        # Output: 12.75  (subarray [12, -5, -6, 50] sums to 51; 51/4 = 12.75)
        #
        # Input: nums = [5], k = 1
        # Output: 5.0
        max_sum = current = sum(nums[:k])
        for i in range(k, len(nums)):
            current -= nums[i - k]
            current += nums[i]
            max_sum = max(max_sum, current)
        return max_sum / k
