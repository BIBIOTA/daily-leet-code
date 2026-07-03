# Hash Table

### From: 1. Two Sum (2026-06-24)

Input: `nums = [2, 7, 11, 15]`, `target = 9`
Approach: 用一個 dict 在遍歷時記錄「已見過的數字 → 索引」，每步計算 `diff = target - num`，若 diff 已在 dict 中即找到答案。
Key insight: 把「找另一半」轉為 O(1) 查找——不需要兩層迴圈，只需一次遍歷。

```
index=0, num=2, diff=7 → dict={} → 未找到 → dict={2:0}
index=1, num=7, diff=2 → dict={2:0} → 找到！→ return [dict[2], 1] = [0,1]
```

Mistake I made: 用 `defaultdict(list)` 但實際存的是 int（不是 list），語意不符；應直接用 `{}`。另外誤用 `dict.append()` 而非 `dict[key] = value`。

進階：若陣列已排序，可改用 Two Pointers（左右各一），時間仍 O(n)，空間降至 O(1)。

---

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

---

### From: 217. Contains Duplicate (2026-06-25)

Input: `[1, 2, 3, 1]`
Approach: 將陣列轉成 set 後比較長度——若長度不同代表有重複。
Key insight: set 只保留唯一值，任何重複都會使 set 長度小於陣列長度。

```
nums = [1, 2, 3, 1]
set(nums) = {1, 2, 3} → len 3
len(nums) = 4
3 != 4 → True
```

Mistake I made: (none)

進階：若不能用額外空間（O(1) space），先 sort 再比較相鄰元素，時間升至 O(n log n)。

---

### From: 49. Group Anagrams — Review (2026-06-29)

Input: `["eat", "tea", "tan", "ate", "nat", "bat"]`
Approach: 用 `defaultdict(list)`，對每個字串 `tuple(sorted(word))` 作為 key，把同 key 的字串 append 在一起，最後 `return list(anagrams_dict.values())`。
Key insight: 互為字母異位詞的字串，排序後字元 tuple 完全相同，可作為 hash map 的 key。時間複雜度是 O(n·k log k)，若要降至 O(n·k) 可改用長度 26 的字母頻率陣列當 key。

Mistake I made: `return [anagrams_dict.values()]` 和 `return [list(...)]` 都多包了一層 `[]`，正確寫法是 `return list(anagrams_dict.values())`。時間複雜度誤答 O(n)，忽略了 `sorted(word)` 的 O(k log k) 成本。

---

### From: 1. Two Sum — Review (2026-06-29)

Input: `nums = [2, 7, 11, 15]`, `target = 9`
Approach: 用 dict 記錄「已遍歷的數字 → 索引」，每步計算 `diff = target - num`，若 diff 在 dict 中即回傳兩索引。
Key insight: 一次遍歷＋O(1) 查找取代兩層迴圈，時間 O(n)、空間 O(n)。

```
index=0, num=2, diff=7 → {} → 未找到 → {2:0}
index=1, num=7, diff=2 → {2:0} → 找到！→ return [0, 1]
```

Mistake I made: `if diff in result.keys()` 多餘，Python 3 直接 `if diff in result` 即可；`else` 分支可刪（if 內已 return）。進階：陣列已排序時改用 Two Pointers，空間降至 O(1)。

---

### From: 49. Group Anagrams — Review (2026-06-30)

Input: `["eat", "tea", "tan", "ate", "nat", "bat"]`
Approach: `defaultdict(list)` 以 `tuple(sorted(word))` 為 key，將同組字串 append 在一起，最後 `return list(anagrams_dict.values())`。
Key insight: 互為異位詞的字串排序後完全相同，可作為 hash map 的 key 聚合分組。

```
"eat" → tuple(sorted) → ('a','e','t') → dict[('a','e','t')] = ["eat"]
"tea" → ('a','e','t') → dict[('a','e','t')] = ["eat","tea"]
"tan" → ('a','n','t') → dict[('a','n','t')] = ["tan"]
"ate" → ('a','e','t') → dict[('a','e','t')] = ["eat","tea","ate"]
"nat" → ('a','n','t') → dict[('a','n','t')] = ["tan","nat"]
"bat" → ('a','b','t') → dict[('a','b','t')] = ["bat"]
→ return [["eat","tea","ate"],["tan","nat"],["bat"]]
```

Mistake I made: `return` 那行連錯三次——先誤用解包語法 `[word for word, _ in ...]`，再誤包 `[anagrams_dict.values()]`，再漏掉 expression 寫成 `[for word in ...]`。正確寫法是 `list(anagrams_dict.values())` 或等價的 `[group for group in anagrams_dict.values()]`（注意變數名應為 `group` 不是 `word`）。時間複雜度誤答 O(n log k)，忘記乘以外層 n；空間複雜度誤答 O(n)，忘記字串本身的長度 m。

進階 key 設計：改用字母頻率陣列，時間從 O(n·m log m) 降至 O(n·m)：
```python
count = [0] * 26
for c in word:
    count[ord(c) - ord('a')] += 1
key = tuple(count)
```

---

### From: 1. Two Sum — Review (2026-06-30)

Input: `nums = [2, 7, 11, 15]`, `target = 9`
Approach: 用 dict 記錄「已遍歷的數字 → 索引」，每步計算 `diff = target - num`，若 diff 在 dict 中即回傳兩索引。
Key insight: hash map 替代了 brute force 的外層迴圈——把「找另一半」轉為 O(1) complement 查找。

```
index=0, num=2, diff=7 → {} → 未找到 → {2:0}
index=1, num=7, diff=2 → {2:0} → 找到！→ return [0, 1]
```

Mistake I made: (none — 乾淨解出，無提示)

進階：陣列已排序時可改用 Two Pointers（left=0, right=n-1），時間仍 O(n)，空間降至 O(1)。

---

### From: 217. Contains Duplicate — Review (2026-06-30)

Input: `[1, 2, 3, 1]`
Approach: `len(set(nums)) != len(nums)` — 建立 set 與原陣列比較長度。
Key insight: set 去重後若長度變小，必有重複——O(n) 時間，O(n) 空間；一行解決。

```
nums = [1, 2, 3, 1]
set(nums) = {1, 2, 3} → len 3
len(nums) = 4
3 != 4 → True
```

Mistake I made: (none — 乾淨解出，無提示；這次也正確說明了空間複雜度 O(n))

---

### From: 217. Contains Duplicate — Review (2026-06-29)

Input: `[1, 2, 3, 1]`
Approach: `len(set(nums)) != len(nums)` — 將陣列轉為 set 後比較長度差異。
Key insight: set 只保留唯一值，若有重複，set 長度必定小於原陣列長度。

```
nums = [1, 2, 3, 1]
set(nums) = {1, 2, 3} → len 3
len(nums) = 4
3 != 4 → True（有重複）
```

Mistake I made: 空間複雜度誤答 O(1)，實際上 `set(nums)` 最多存放 n 個元素，空間為 O(n)。O(1) 空間需先 in-place sort 再比較相鄰元素，但時間升至 O(n log n)。

---

### From: 49. Group Anagrams — Review (2026-07-01)

Input: `["eat","tea","tan","ate","nat","bat"]`
Approach: `defaultdict(list)` 以 `tuple(sorted(word))` 為 key，將同組字串 append 在一起，最後 `return list(anagrams_dict.values())`。
Key insight: 互為異位詞的字串排序後字元 tuple 完全相同，可作為 hash map 的分組 key；時間 O(n·k log k)，空間 O(n·k)。

```
"eat" → ('a','e','t') → dict[('a','e','t')] = ["eat"]
"tea" → ('a','e','t') → dict[('a','e','t')] = ["eat","tea"]
"tan" → ('a','n','t') → dict[('a','n','t')] = ["tan"]
"ate" → ('a','e','t') → dict[('a','e','t')] = ["eat","tea","ate"]
"nat" → ('a','n','t') → dict[('a','n','t')] = ["tan","nat"]
"bat" → ('a','b','t') → dict[('a','b','t')] = ["bat"]
→ return [["eat","tea","ate"],["tan","nat"],["bat"]]
```

Mistake I made: (none — 乾淨解出，無提示)

進階優化：改用 26-element 字母頻率 tuple 當 key，時間從 O(n·k log k) 降至 O(n·k)：
```python
count = [0] * 26
for c in word:
    count[ord(c) - ord('a')] += 1
key = tuple(count)
```

---

### From: 1. Two Sum — Review (2026-07-03)

Input: `nums = [2, 7, 11, 15]`, `target = 9`
Approach: 用 dict 記錄「已遍歷的數字 → 索引」，每步計算 `diff = target - num`，若 diff 在 dict 中即回傳兩索引。
Key insight: hash map 把「找另一半」轉為 O(1) complement 查找，時間 O(n)、空間 O(n)；若陣列已排序，改用 Two Pointers 可將空間降至 O(1)。

```
index=0, num=2, diff=7 → {} → 未找到 → {2:0}
index=1, num=7, diff=2 → {2:0} → 找到！→ return [0, 1]
```

Mistake I made: (none — 乾淨解出，無提示)
