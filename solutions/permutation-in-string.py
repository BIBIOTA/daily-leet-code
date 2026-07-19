from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Examples:
        # checkInclusion("ab", "eidbaooo") -> True  ("ba" is a permutation of "ab" appears in s2)
        # checkInclusion("ab", "eidboaoo") -> False
        s1_len = len(s1)
        s2_len = len(s2)

        if s1_len > s2_len:
            return False

        s1_count = Counter(s1)
        s2_count = Counter(s2[:len(s1)])

        if s1_count == s2_count:
            return True

        for i in range(s1_len, s2_len):
            s2_count[s2[i - s1_len]] -= 1
            s2_count[s2[i]] += 1
            if s2_count[s2[i - s1_len]] == 0:
                del s2_count[s2[i - s1_len]]

            if s2_count == s1_count:
                return True
        return False
