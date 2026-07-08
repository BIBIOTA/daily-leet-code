class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        # Examples:
        # Input: s = "book"     → a = "bo", b = "ok"   → vowels: 1 vs 1 → True
        # Input: s = "textbook" → a = "text", b = "book" → vowels: 1 vs 2 → False
        vowels = set('aeiouAEIOU')
        middle = len(s) // 2
        front, back = s[:middle], s[middle:]
        return sum(vowel in vowels for vowel in front) == sum(vowel in vowels for vowel in back)