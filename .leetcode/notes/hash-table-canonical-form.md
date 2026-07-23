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

---

### From: 49. Group Anagrams (2026-07-08) — 複習

Input: `["eat", "tea", "tan", "ate", "nat", "bat"]`
Approach: 與上次相同：`tuple(sorted(word))` 作為 key，`defaultdict(list)` 分組，回傳 `list(anagrams_dict.values())`。
Key insight: 這次成功在 rung 0 通過；複雜度也答對（O(n·k log k) / O(n·k)）。

Mistake I made: `from collection import defaultdict` typo（少一個 s），導致 /run 第一次 NameError。

---

### From: 49. Group Anagrams (2026-07-10) — 複習

Input: `["eat", "tea", "tan", "ate", "nat", "bat"]`
Approach: `tuple(sorted(word))` 作為 key，`defaultdict(list)` 分組，回傳 `list(groups.values())`。
Key insight: return 階段直接取 `.values()` 即可；對 dict 本身迭代只拿到 keys。

Mistake I made: return 誤寫為 `[word for word, _ in groups]`。`groups` 是 dict，對 dict 迭代拿到的是 key（字元 tuple），嘗試解包成 2 個值 → ValueError。正確寫法是 `list(groups.values())`。要記得 `collections`（複數）。

---

### From: 49. Group Anagrams (2026-07-15) — 複習

Input: `["eat", "tea", "tan", "ate", "nat", "bat"]`
Approach: `tuple(sorted(word))` 作為 key，`defaultdict(list)` 分組，回傳 `list(results.values())`。
Key insight: 排序後結果相同的字串就是 anagram，排序即 canonical form。

Mistake I made: `defaultdict` 使用了但沒有 `from collections import defaultdict`，第一次 /run 即 NameError。pattern 只答 Hash Table，應完整答 Hash Table + Canonical Form。

---

### From: 49. Group Anagrams (2026-07-23) — 複習

Input: `["eat", "tea", "tan", "ate", "nat", "bat"]`
Approach: `tuple(sorted(word))` 作為 key，`defaultdict(list)` 分組，回傳 `list(group.values())`。
Key insight: `sorted()` 回傳 `list`，list 不可 hash；必須轉為 `tuple` 才能作為 dict key。

Mistake I made: 第一版寫 `key = sorted(word)`（list），觸發 `TypeError: cannot use 'list' as a dict key`；改為 `tuple(sorted(word))` 即修正。複雜度與頻率 tuple 優化皆正確答出。
