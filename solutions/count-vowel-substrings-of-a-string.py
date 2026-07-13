class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        # Examples:
        #   word = "aeiouu"        -> 2
        #   word = "unicornarihan" -> 0
        #   word = "cuaieuouac"    -> 7
        #
        # Constraints:
        #   1 <= len(word) <= 100
        #   word consists of lowercase English letters only.
        vowels = set('aeiou')
        left = start = results = 0
        freq = defaultdict(int)
        for right in range(len(word)):
            if word[right] in vowels:
                freq[word[right]] += 1
            else:
                left = start = right + 1
                freq = defaultdict(int)
            while len(freq) == 5:
                freq[word[start]] -= 1
                if freq[word[start]] == 0:
                    del freq[word[start]]
                start += 1
            results += start - left
        return results
