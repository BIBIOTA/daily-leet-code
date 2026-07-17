class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        # Examples:
        # Input: s = "book"      -> Output: True
        #   first half "bo" has 1 vowel, second half "ok" has 1 vowel => equal
        #
        # Input: s = "textbook"  -> Output: False
        #   first half "text" has 1 vowel, second half "book" has 2 vowels => not equal
        mid = len(s) // 2
        front, back = s[:mid], s[mid:]
        vowels = set('aeiouAEIOU')
        return sum(ch in vowels for ch in front) == sum(ch in vowels for ch in back)
