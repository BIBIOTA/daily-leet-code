class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # Examples:
        # Input: s = "abciiidef", k = 3  -> Output: 3  (substring "iii")
        # Input: s = "aeiou", k = 2      -> Output: 2  (any 2-char window has 2 vowels)
        # Input: s = "leetcode", k = 3   -> Output: 2  ("lee", "eet", "ode" all have 2)
        vowels = set('aeiou')
        max_vowels = curr = sum(ch in vowels for ch in s[:k])
        for i in range(k, len(s)):
            if s[i - k] in vowels:
                curr -= 1
            if s[i] in vowels:
                curr += 1
            max_vowels = max(curr, max_vowels)
        return max_vowels