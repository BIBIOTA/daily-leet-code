from typing import List
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s), len(p)
        if p_len > s_len:
            return []

        p_count = Counter(p)
        s_count = Counter(s[:p_len])  # 第一個視窗
        results = []

        if s_count == p_count:
            results.append(0)

        for i in range(1, s_len - p_len + 1):
            # 移除左端離開的字元
            left = s[i - 1]
            s_count[left] -= 1
            if s_count[left] == 0:
                del s_count[left]

            # 加入右端新進入的字元
            s_count[s[i + p_len - 1]] += 1

            if s_count == p_count:
                results.append(i)

        return results