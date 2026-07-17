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
        sub_strings = defaultdict(int)
        left = start = results = 0
        for right in range(len(word)):
            if word[right] in vowels:
                sub_strings[word[right]] += 1
            else:
                left = start = right + 1
                sub_strings = defaultdict(int)
            while len(sub_strings) == 5:
                sub_strings[word[start]] -= 1
                if sub_strings[word[start]] == 0:
                    del sub_strings[word[start]]
                start += 1
            results += start - left
        return results