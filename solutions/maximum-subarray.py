from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        max_result = current = nums[0]

        for num in nums[1:]:
            current = max(num, current + num)
            max_result = max(max_result, current)
        return max_result

# Examples (paraphrased):
# [-2, 1, -3, 4, -1, 2, 1, -5, 4] -> 6
# [1] -> 1
# [5, 4, -1, 7, 8] -> 23
