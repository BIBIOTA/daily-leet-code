from typing import List
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Examples:
        # Input: s = "cbaebabacd", p = "abc" -> Output: [0, 6]
        #   "cba" starts at index 0, "bac" starts at index 6
        # Input: s = "abab", p = "ab" -> Output: [0, 1, 2]
        #   "ab" at 0, "ba" at 1, "ab" at 2
        p_count = Counter(p)
        p_len = len(p)
        s_len = len(s)
        results = []
        for i in range(s_len):
            if i + p_len > s_len:
                break
            if p_count == Counter(s[i:i + p_len]):
                results.append(i)
        return results