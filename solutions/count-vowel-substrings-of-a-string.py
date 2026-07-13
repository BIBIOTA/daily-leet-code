from collections import defaultdict
# 2062. Count Vowel Substrings of a String (Easy)
#
# Examples:
#   word = "aeiouu"        -> 2
#   word = "unicornarihan" -> 0
#   word = "aeioubbb"      -> 1
#
# Constraints:
#   1 <= len(word) <= 100
#   word consists of lowercase English letters only.


class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = set('aeiou')
        vowel_count = defaultdict(int)
        left = inner_left = sum_results = 0
        for right in range(len(word)):
            if word[right] in vowels:
                vowel_count[word[right]] += 1
            else:
                vowel_count = defaultdict(int)
                inner_left = left = right + 1
            while len(vowel_count) == 5:
                vowel_count[word[inner_left]] -= 1
                if vowel_count[word[inner_left]] == 0:
                    del vowel_count[word[inner_left]]
                inner_left += 1
            sum_results += inner_left - left
        return sum_results