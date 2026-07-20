from collections import defaultdict

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        # Examples:
        # word = "aeiouu"        -> 2
        # word = "unicornarihan" -> 0
        # word = "cuaieuouac"    -> 7
        # word = "bbaeixoubb"    -> 0
        #
        # Constraints:
        #   1 <= len(word) <= 100
        #   word consists of lowercase English letters only.
        vowels = set('aeiou')
        result = left = start = 0
        substrings = defaultdict(int)
        for right in range(len(word)):
            if word[right] in vowels:
                substrings[word[right]] += 1
            else:
                substrings = defaultdict(int)
                start = left = right + 1
            while len(substrings) == 5:
                substrings[word[start]] -= 1
                if substrings[word[start]] == 0:
                    del substrings[word[start]]
                start += 1
            result += start - left
        return result