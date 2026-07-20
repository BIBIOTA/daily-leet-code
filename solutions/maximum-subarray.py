from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_array = current = nums[0]
        for i in range(1, len(nums)):
            current = max(current + nums[i], nums[i])
            sum_array = max(current, sum_array)
        return sum_array

# Examples:
# Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output: 6  (subarray [4, -1, 2, 1])

# Input: nums = [1]
# Output: 1

# Input: nums = [5, 4, -1, 7, 8]
# Output: 23  (entire array)
