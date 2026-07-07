# Hash Table + Canonical Form

## Pattern Summary

把每個元素轉換成「標準形式（canonical form）」作為 Hash Table 的 key，讓具有相同本質的元素被分在同一組。

---

### From: 49. Group Anagrams (2026-07-07)

Input: `["eat", "tea", "tan", "ate", "nat", "bat"]`
Approach: 對每個字串排序後轉成 tuple 作為 key，用 defaultdict(list) 把同 key 的字串收集在一起，最後回傳所有 values。
Key insight: anagram 排序後必定相同，排序結果就是 canonical form。

Trace:
```
"eat" → sorted → ('a','e','t') → key
"tea" → sorted → ('a','e','t') → 同 key → 同組
"tan" → sorted → ('a','n','t') → 不同 key → 新組
```

Mistake I made: 使用 `defaultdict` 但忘記 `from collections import defaultdict`，實際提交會 NameError。
時間複雜度誤答 O(n·k)，應為 O(n·k log k)（排序每個字串需 O(k log k)）。
O(n·k) 做法：改用 26-element 字元計數 tuple 當 key，避免排序。

```python
# O(n·k) 優化版
count = [0] * 26
for c in word:
    count[ord(c) - ord('a')] += 1
key = tuple(count)
```
