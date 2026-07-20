from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Examples:
        # checkInclusion("ab", "eidbaooo") -> True   (s2 contains "ba", which is a permutation of "ab")
        # checkInclusion("ab", "eidboaoo") -> False
        s1_len = len(s1)
        s2_len = len(s2)

        if s1_len > s2_len:
            return False

        s1_count = Counter(s1)
        s2_count = Counter(s2[:s1_len])

        if s1_count == s2_count:
            return True

        for i in range(1, s2_len - s1_len + 1):
            left = s2[i - 1]
            s2_count[left] -= 1
            if s2_count[left] == 0:
                del s2_count[left]
            right = s2[i + s1_len - 1]
            s2_count[right] += 1
            if s1_count == s2_count:
                return True
        return False

