from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # Examples:
        # Input: nums = [1, 2, 3, 1]    -> Output: 4   (選 index 0 + index 2 = 1 + 3)
        # Input: nums = [2, 7, 9, 3, 1] -> Output: 12  (選 index 0 + index 2 + index 4 = 2 + 9 + 1)
        prev_1 = prev_2 = 0
        for num in nums:
            curr = num + prev_2
            prev_2 = prev_1
            prev_1 = max(curr, prev_2)
        return prev_1