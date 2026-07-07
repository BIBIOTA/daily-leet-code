from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Examples:
        # Input: [1, 2, 3, 1]              -> True  (1 appears twice)
        # Input: [1, 2, 3, 4]              -> False (all distinct)
        # Input: [1, 1, 1, 3, 3, 4, 3, 2, 4, 2] -> True
        return len(set(nums)) != len(nums)
