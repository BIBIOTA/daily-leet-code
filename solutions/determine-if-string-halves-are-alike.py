class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        # Examples:
        # Input: s = "book"  -> a = "bo", b = "ok"  -> Output: True  (each half has 1 vowel)
        # Input: s = "textbook" -> a = "text", b = "book" -> Output: False (1 vs 2 vowels)
        vowels = set('aeiou')
        mid_len = len(s) // 2
        front, back = s[mid_len:], s[:mid_len]
        front_vowels_count = sum(char in vowels for char in front.lower())
        back_vowels_count = sum(char in vowels for char in back.lower())

        return front_vowels_count == back_vowels_count
