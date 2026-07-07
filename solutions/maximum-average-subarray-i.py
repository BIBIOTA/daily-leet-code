from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current = sum(nums[:k])
        max_sum = current
        for i in range(k, len(nums)):            
            window_sum = current - nums[i - k] + nums[i]
            max_sum = max(window_sum, max_sum)
            current = window_sum
        return max_sum / k


# Examples:
# Input: nums = [1, 12, -5, -6, 50, 3], k = 4
# Output: 12.75000
# Explanation: 某段長度為 4 的連續子陣列，其元素平均值最大為 12.75

# Input: nums = [5], k = 1
# Output: 5.00000
