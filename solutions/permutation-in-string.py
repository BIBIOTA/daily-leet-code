from typing import List
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Examples:
        # checkInclusion("ab", "eidbaooo") -> True   (s2 中含有 "ba"，是 s1 的一種排列)
        # checkInclusion("ab", "eidboaoo") -> False
        s1_len = len(s1)
        s2_len = len(s2)

        if s1_len > s2_len:
            return False

        s1_check = Counter(s1)
        start = s2[:s1_len]

        if Counter(start) == s1_check:
            return True

        for i in range(s1_len, s2_len):
            start = start[1:] + s2[i]
            if Counter(start) == s1_check:
                return True
        return False
