from typing import List
from collections import Counter


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k, len(nums)):
            window_sum += nums[i]
            window_sum -= nums[i - k]
            max_sum = max(max_sum, window_sum)
        return max_sum / k

# Examples:
# Input: nums = [1, 12, -5, -6, 50, 3], k = 4
# Output: 12.75000
# Explanation: 子陣列 [12, -5, -6, 50] 的平均值為 51 / 4 = 12.75

# Input: nums = [5], k = 1
# Output: 5.00000
