from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_nums = Counter(nums).most_common(k)
        
        return [num for num, _ in counter_nums]