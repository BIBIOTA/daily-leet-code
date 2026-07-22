from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Examples:
        # Input: nums = [3,4,5,1,2]  -> Output: 1
        # Input: nums = [4,5,6,7,0,1,2] -> Output: 0
        # Input: nums = [11,13,15,17] -> Output: 11
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (right + left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[right]