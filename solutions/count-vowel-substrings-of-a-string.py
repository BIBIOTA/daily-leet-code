# 2062. Count Vowel Substrings of a String (Easy)
#
# Examples:
#   word = "aeiouu"        -> 2
#   word = "unicornarihan" -> 0
#   word = "cuaieuouac"    -> 7
#
# Constraints:
#   1 <= len(word) <= 100
#   word consists of lowercase English letters only.


class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowel_dict = {}
        result = 0
        have = 0
        left = start = 0
        for right, ch in enumerate(word):
            if ch not in set('aeiou'):
                vowel_dict = {}
                have = 0
                left = start = right + 1
                continue

            vowel_dict[ch] = vowel_dict.get(ch, 0) + 1

            if vowel_dict[ch] == 1:
                have += 1

            while have == 5:
                start_ch = word[start]
                vowel_dict[start_ch] -= 1

                if vowel_dict[start_ch] == 0:
                    have -= 1
                start += 1
            result += start - left

        return result