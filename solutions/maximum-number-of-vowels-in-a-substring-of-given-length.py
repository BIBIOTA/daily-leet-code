from typing import List


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # Examples:
        # Input: s = "abciiidef", k = 3 -> Output: 3  ("iii" 包含 3 個母音)
        # Input: s = "aeiou", k = 2     -> Output: 2  (任意長度 2 的子字串都含 2 個母音)
        # Input: s = "leetcode", k = 3  -> Output: 2  ("lee", "eet", "ode" 各含 2 個母音)
        vowels = set('aeiou')
        last_count = sum(ch in vowels for ch in s[:k])
        max_count = last_count
        for i in range(k, len(s)):
            window_count = last_count

            if s[i - k] in vowels:
                window_count -= 1

            if s[i] in vowels:
                window_count += 1

            last_count = window_count
            max_count = max(window_count, max_count)
        return max_count
