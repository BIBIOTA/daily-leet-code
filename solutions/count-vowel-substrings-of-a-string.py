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
        vowels = set('aeiou')
        res = 0
        cnt = {}          # 視窗內每種母音的出現次數
        have = 0          # 視窗內「不同母音」的種類數
        left = 0          # 當前連續母音段的左界
        start = left      # 收縮指標

        for right, ch in enumerate(word):
            if ch not in vowels:          # 碰到子音 -> 整段重置
                cnt.clear()
                have = 0
                left = start = right + 1
                continue

            cnt[ch] = cnt.get(ch, 0) + 1
            if cnt[ch] == 1:              # 這種母音第一次進視窗
                have += 1

            while have == 5:              # 集滿了 -> 從 start 端往右縮
                c = word[start]
                cnt[c] -= 1
                if cnt[c] == 0:
                    have -= 1
                start += 1

            res += start - left           # 合法起點個數
        return res
