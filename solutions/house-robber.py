from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        prev_2 = 0
        prev_1 = 0

        for num in nums:
            current = num + prev_2
            prev_2 = prev_1
            prev_1 = max(current, prev_1)
        return max(prev_1, prev_2)

# Examples:
# nums = [1, 2, 3, 1]        -> 4   (偷 house 0 與 house 2 = 1 + 3)
# nums = [2, 7, 9, 3, 1]     -> 12  (偷 house 0, 2, 4 = 2 + 9 + 1)
