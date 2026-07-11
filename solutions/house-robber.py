from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # Examples:
        # Input: nums = [1, 2, 3, 1]    -> Output: 4   (選 index 0 + index 2 = 1 + 3)
        # Input: nums = [2, 7, 9, 3, 1] -> Output: 12  (選 index 0 + index 2 + index 4 = 2 + 9 + 1)
        prev = curr = 0
        for num in nums:
            prev, curr = curr, max(curr, num + prev)
        return curr
