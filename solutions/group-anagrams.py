from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list)
        for word in strs:
            key = tuple(sorted(word))
            anagrams_dict[key].append(word)
        return list(anagrams_dict.values())


# Examples:
# Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]  (任意順序皆可)
#
# Input: strs = [""]
# Output: [[""]]
#
# Input: strs = ["a"]
# Output: [["a"]]
