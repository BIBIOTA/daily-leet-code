from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Examples:
        # Input: nums = [1,1,1,2,2,3], k = 2  => Output: [1, 2]
        # Input: nums = [1], k = 1             => Output: [1]
        frequent_k = Counter(nums).most_common(k)
        return [num for num,_ in frequent_k]
