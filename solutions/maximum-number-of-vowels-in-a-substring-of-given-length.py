from typing import List


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # Examples:
        # Input: s = "abciiidef", k = 3  -> Output: 3  ("iii" 含 3 個母音)
        # Input: s = "aeiou", k = 2      -> Output: 2  (任何長度 2 的子字串都含 2 個母音)
        # Input: s = "leetcode", k = 3   -> Output: 2  ("lee", "eet", "ode" 各含 2 個母音)
        vowels = set('aeiou')
        current = max_count = sum(ch in vowels for ch in s[:k])
        for i in range(k, len(s)):
            if s[i - k] in vowels:
                current -= 1
            if s[i] in vowels:
                current += 1
            max_count = max(current, max_count)
        return max_count
