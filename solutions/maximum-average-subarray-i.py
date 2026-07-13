from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Examples:
        # Input: nums = [1, 12, -5, -6, 50, 3], k = 4
        # Output: 12.75  (subarray [12, -5, -6, 50], sum = 51, avg = 12.75)
        #
        # Input: nums = [5], k = 1
        # Output: 5.0
        max_sum = current = sum(nums[:k])
        for i in range(k, len(nums)):
            current -= nums[i - k]
            current += nums[i]
            max_sum = max(current, max_sum)
        return max_sum / k
