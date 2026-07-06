from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # Examples:
        # Input: nums = [1, 2, 3, 1]  → Output: 4
        # Input: nums = [2, 7, 9, 3, 1] → Output: 12
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        # 建立 dp 陣列，長度與 nums 相同，初始全為 0
        dp = [0] * len(nums)

        # base cases
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        # 由左往右填 dp
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp[- 1]