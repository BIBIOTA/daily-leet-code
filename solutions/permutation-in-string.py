from typing import List
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Examples:
        # checkInclusion("ab", "eidbaooo") -> True
        # checkInclusion("ab", "eidboaoo") -> False
        s1_len = len(s1)
        s2_len = len(s2)

        if s1_len > s2_len:
            return False

        s1_count = Counter(s1)
        s2_count = Counter(s2[:s1_len])

        if s1_count == s2_count:
            return True

        for i in range(s1_len, s2_len):
            first_key = s2[i - s1_len]
            s2_count[first_key] -= 1
            if s2_count[first_key] == 0:
                del s2_count[first_key]

            s2_count[s2[i]] += 1
            if s1_count == s2_count:
                return True
        return False
        
