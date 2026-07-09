from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = last_sum = sum(nums[:k])
        for i in range(k, len(nums)):
            current = last_sum
            current -= nums[i - k]
            current += nums[i]
            last_sum = current
            max_sum = max(current, max_sum)
        return max_sum / k


# Examples:
# nums = [1, 12, -5, -6, 50, 3], k = 4  ->  12.75000
