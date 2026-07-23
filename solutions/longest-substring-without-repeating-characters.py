class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Examples:
        # Input: s = "abcabcbb" -> Output: 3  (e.g. "abc")
        # Input: s = "bbbbb"    -> Output: 1  (e.g. "b")
        # Input: s = "pwwkew"   -> Output: 3  (e.g. "wke")
        left = max_len = 0
        window = set()
        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left += 1
            window.add(s[right])
            max_len = max(max_len, len(window))
        return max_len
