from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Examples:
        # Input: nums = [1,1,1,2,2,3], k = 2  →  Output: [1, 2]
        # Input: nums = [1], k = 1             →  Output: [1]
        nums_count = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        results = []
        for num, count in nums_count.items():
            buckets[count].append(num)
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                results.append(num)
                if len(results) == k:
                    return results
        return results
