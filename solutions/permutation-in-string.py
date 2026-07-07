from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Examples:
        # checkInclusion("ab", "eidbaooo") -> True   ("ba" is a permutation of "ab")
        # checkInclusion("ab", "eidboaoo") -> False
        s1_len = len(s1)
        s2_len = len(s2)
        if s1_len > s2_len:
            return False
        
        s1_counter = Counter(s1)
        s2_counter = Counter(s2[:s1_len])

        if s1_counter == s2_counter:
            return True
        
        for i in range(s1_len, s2_len):
            last_ch = s2[i - s1_len]

            s2_counter[last_ch] -= 1
            s2_counter[s2[i]] += 1

            if s2_counter[last_ch] == 0:
                del s2_counter[last_ch]

            if s1_counter == s2_counter:
                return True
        return False
