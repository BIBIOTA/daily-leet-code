from typing import List
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Examples:
        # Input: s1 = "ab", s2 = "eidbaooo" -> Output: True  (s2 含有 "ba"，是 s1 的一種排列)
        # Input: s1 = "ab", s2 = "eidboaoo" -> Output: False
        n = len(s1)
        if n > len(s2):
            return False

        s1c, win = Counter(s1), Counter(s2[:n])

        for i in range(n, len(s2)):
            if win == s1c:
                return True
            win[s2[i]] += 1
            win[s2[i - n]] -= 1
            if win[s2[i - n]] == 0:
                del win[s2[i - n]]

        return win == s1c