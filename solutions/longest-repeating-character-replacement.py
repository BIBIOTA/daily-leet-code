from typing import List
from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        left = 0
        max_freq = max_window = 0
        for right in range(len(s)):
            count[s[right]] += 1
            max_freq = max(max_freq, count[s[right]])
            window_size = right - left + 1
            if window_size - max_freq > k:
                count[s[left]] -= 1
                left += 1
            max_window = max(max_window, right - left + 1)
        return max_window


# Examples:
# characterReplacement("ABAB", 2) -> 4
#   將兩個 'A' 換成 'B'（或反過來），得到 "BBBB"
# characterReplacement("AABABBA", 1) -> 4
#   將中間的 'A' 換成 'B'，得到 "AABBBBA"，其中 "BBBB" 是最長的重複字母子字串
