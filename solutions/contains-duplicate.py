from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


# Examples:
# Input: nums = [1, 2, 3, 1]              -> Output: True
# Input: nums = [1, 2, 3, 4]              -> Output: False
# Input: nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2] -> Output: True
