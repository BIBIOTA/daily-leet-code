class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        # Examples:
        # Input: s = "book"     → a = "bo", b = "ok"   → vowels: 1 vs 1 → True
        # Input: s = "textbook" → a = "text", b = "book" → vowels: 1 vs 2 → False
        mid = len(s) // 2
        front, back = s[:mid], s[mid:]
        vowels = set('aeiouAEIOU')
        front_count = sum(ch in vowels for ch in front)
        back_count = sum(ch in vowels for ch in back)
        return front_count == back_count
