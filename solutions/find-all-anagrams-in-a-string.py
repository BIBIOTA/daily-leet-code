from typing import List
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Examples:
        # Input: s = "cbaebabacd", p = "abc" -> Output: [0, 6]
        #   s 中所有以索引 0、6 開頭、長度為 3 的子字串是 p 的易位詞
        #
        # Input: s = "abab", p = "ab" -> Output: [0, 1, 2]
        #   s 中所有以索引 0、1、2 開頭、長度為 2 的子字串是 p 的易位詞
        s_len = len(s)
        p_len = len(p)

        results = []

        if p_len > s_len:
            return []

        s_count = Counter(s[:p_len])
        p_count = Counter(p)

        if s_count == p_count:
            results.append(0)

        for i in range(1, s_len - p_len + 1):
            left = s[i - 1]
            s_count[left] -= 1
            if s_count[left] == 0:
                del s_count[left]
            right = s[i + p_len - 1]
            s_count[right] += 1
            if s_count == p_count:
                results.append(i)
        return results