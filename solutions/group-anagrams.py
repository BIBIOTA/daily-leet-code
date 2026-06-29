from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Examples:
        # Input: ["eat","tea","tan","ate","nat","bat"]
        # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
        #
        # Input: [""]
        # Output: [[""]]
        #
        # Input: ["a"]
        # Output: [["a"]]
        anagrams_dict = defaultdict(list)
        for word in strs:
            key = tuple(sorted(word))
            anagrams_dict[key].append(word)
        return list(anagrams_dict.values())
