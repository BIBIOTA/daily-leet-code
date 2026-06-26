from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = nums[0]
        current = nums[0]
        for num in nums[1:]:
            current = max(current + num, num)
            best = max(current, best)
        return best


        # Examples:
        # Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  -> Output: 6  (subarray: [4,-1,2,1])
        # Input: nums = [1]                                -> Output: 1
        # Input: nums = [5, 4, -1, 7, 8]                  -> Output: 23 (whole array)
        pass
