from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent_k = Counter(nums).most_common(k)
        return [num for num, _ in frequent_k]


# Examples:
# 1) nums = [1, 1, 1, 2, 2, 3], k = 2  ->  [1, 2]
#    (1 出現 3 次、2 出現 2 次，最常出現的前 2 個)
# 2) nums = [1], k = 1  ->  [1]
#
# Constraints:
# - 1 <= nums.length <= 10^5
# - -10^4 <= nums[i] <= 10^4
# - k 在 [1, 陣列中不同數字的數量] 範圍內
# - 答案唯一
# - 回傳順序不限
