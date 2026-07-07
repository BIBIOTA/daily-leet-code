from typing import List


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # Examples:
        # Input: s = "abciiidef", k = 3  -> Output: 3
        # Input: s = "aeiou", k = 2      -> Output: 2
        # Input: s = "leetcode", k = 3   -> Output: 2
        vowels = set('aeiou')
        last_count = sum(vowel in vowels for vowel in s[:k])
        max_count = last_count
        for i in range(k, len(s)):
            window_count = last_count
            if s[i - k] in vowels:
                window_count -= 1
            if s[i] in vowels:
                window_count += 1
            last_count = window_count
            max_count = max(max_count, window_count)
        return max_count
