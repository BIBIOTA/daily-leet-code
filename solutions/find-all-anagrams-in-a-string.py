from typing import List
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Examples:
        # Input: s = "cbaebabacd", p = "abc" -> Output: [0, 6]
        #   "cba" (index 0) and "bac" (index 6) are anagrams of "abc"
        #
        # Input: s = "abab", p = "ab" -> Output: [0, 1, 2]
        #   "ab" (0), "ba" (1), "ab" (2) are all anagrams of "ab"
        s_len = len(s)
        p_len = len(p)
        p_count = Counter(p)
        s_count = Counter(s[:p_len])
        output = []

        if p_count == s_count:
            output.append(0)

        for i in range(1, s_len - p_len + 1):
            left = s[i - 1]
            s_count[left] -= 1
            if s_count[left] == 0:
                del s_count[left]
            right = s[i + p_len - 1]
            s_count[right] += 1
            if s_count == p_count:
                output.append(i)
        return output