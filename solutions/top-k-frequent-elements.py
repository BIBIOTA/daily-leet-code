from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Examples:
        # 1) nums = [1, 1, 1, 2, 2, 3], k = 2  ->  [1, 2]
        #    (1 出現 3 次、2 出現 2 次，最常出現的前 2 個)
        # 2) nums = [1], k = 1  ->  [1]
        #
        # Constraints:
        # - 1 <= nums.length <= 10^5
        # - -10^4 <= nums[i] <= 10^4
        # - k 在 [1, 陣列中不同數字的數量] 範圍內
        # - 答案唯一，回傳順序不限
        # - Follow-up：時間複雜度需優於 O(n log n)
        buckets = [[] for i in range(len(nums) + 1)]
        freq = defaultdict(int)
        result = []
        for num in nums:
            freq[num] += 1
        for num, count in freq.items():
            buckets[count].append(num)
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
            if len(result) == k:
                return result

        