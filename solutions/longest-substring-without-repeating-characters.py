class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Examples:
        # Input: s = "abcabcbb" -> Output: 3
        # Input: s = "bbbbb"    -> Output: 1
        # Input: s = "pwwkew"   -> Output: 3
        max_len = left = 0
        last_seen = {}

        for right in range(len(s)):
            c = s[right]
            if c in last_seen and last_seen[c] >= left:
                left = last_seen[c] + 1
            last_seen[c] = right
            max_len = max(max_len, right - left + 1)
        return max_len