from typing import List
from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Examples:
        # Input: s = "abcabcbb" -> Output: 3  ("abc")
        # Input: s = "bbbbb"    -> Output: 1  ("b")
        # Input: s = "pwwkew"   -> Output: 3  ("wke")
        max_len = left = 0
        char_index = {}
        for right, ch in enumerate(s):
            if ch in char_index and char_index[ch] >= left:
                left = char_index[ch] + 1
            char_index[ch] = right
            max_len = max(max_len, right - left + 1)
        return max_len
