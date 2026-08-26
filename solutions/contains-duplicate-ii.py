from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()

        for i in range(len(nums)):
            if nums[i] in window:
                return True
            window.add(nums[i])

            if len(window) > k:
                window.remove(nums[i - k])
        return False


# Examples:
# nums = [1, 2, 3, 1], k = 3        -> True   (兩個 1 的索引 0 與 3，差 3 <= k)
# nums = [1, 0, 1, 1], k = 1        -> True   (索引 2 與 3 的 1，差 1 <= k)
# nums = [1, 2, 3, 1, 2, 3], k = 2  -> False  (相同數字最近也差 3 > k)
#
# Constraints:
# 1 <= len(nums) <= 10^5
# -10^9 <= nums[i] <= 10^9
# 0 <= k <= 10^5
