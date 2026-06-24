# Hash Table

### From: 49. Group Anagrams (2026-06-24)

Input: `["eat", "tea", "tan", "ate", "nat", "bat"]`
Approach: 用 `defaultdict(list)`，對每個字串排序後的字母作為 key，把原字串 append 進同一個 list。
Key insight: 字母異位詞排序後一定相同，排序後的字母可作為唯一識別 key。

```
"eat" → sorted → ('a','e','t') → group_dict[('a','e','t')] = ["eat"]
"tea" → sorted → ('a','e','t') → group_dict[('a','e','t')] = ["eat","tea"]
"tan" → sorted → ('a','n','t') → group_dict[('a','n','t')] = ["tan"]
"ate" → sorted → ('a','e','t') → group_dict[('a','e','t')] = ["eat","tea","ate"]
...
```

Mistake I made: 誤以為 Python `str` 是可變的（mutable），實際上 str 和 tuple 都是 immutable，都能當 dict key；選 tuple 的真正優勢是省掉 `"".join()` 步驟。

進階：若要進一步從 O(k log k) 降到 O(k)，可改用字母頻率陣列當 key：
```python
count = [0] * 26
for c in word:
    count[ord(c) - ord('a')] += 1
key = tuple(count)
```
