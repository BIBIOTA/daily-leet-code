from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = defaultdict(list)
        for word in strs:
            key = tuple(sorted(word))
            results[key].append(word)
        return list(results.values())


# Examples:
# Input:  strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["bat"], ["nat","tan"], ["ate","eat","tea"]]  (any order)
#
# Input:  strs = [""]
# Output: [[""]]
#
# Input:  strs = ["a"]
# Output: [["a"]]
