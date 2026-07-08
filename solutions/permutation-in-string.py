from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Examples:
        # checkInclusion("ab", "eidbaooo") -> True   ("ba" is a permutation of "ab")
        # checkInclusion("ab", "eidboaoo") -> False
        if len(s1) > len(s2):
            return False
        
        check = s2[:len(s1)]

        if Counter(s1) == Counter(check):
            return True

        for i in range(len(s1), len(s2)):
            check = check[1:] + s2[i]
            if Counter(s1) == Counter(check):
                return True
        return False
