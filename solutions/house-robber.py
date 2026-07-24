from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # Examples:
        # Input: nums = [1, 2, 3, 1]  →  Output: 4
        #   (取る: house[0]=1, house[2]=3 → 合計 4)
        #
        # Input: nums = [2, 7, 9, 3, 1]  →  Output: 12
        #   (取る: house[0]=2, house[2]=9, house[4]=1 → 合計 12)
        prev_1 = prev_2 = 0
        for i in range(len(nums)):
            curr = nums[i] + prev_2
            prev_2 = prev_1
            prev_1 = max(prev_1, curr)
        return prev_1