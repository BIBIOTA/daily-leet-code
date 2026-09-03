from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Examples:
        # checkInclusion("ab", "eidbaooo") -> True
        # 「ba」由 s1 的字元重新排列而成，且出現在 s2 中。
        # checkInclusion("ab", "eidboaoo") -> False
        s1_count = Counter(s1)
        s2_count = Counter(s2[:len(s1)])

        if s1_count == s2_count:
            return True

        for i in range(len(s1), len(s2)):
            last = s2[i - len(s1)]
            s2_count[last] -= 1
            if s2_count[last] == 0:
                del s2_count[last]
            s2_count[s2[i]] += 1
            if s1_count == s2_count:
                return True
        return False
