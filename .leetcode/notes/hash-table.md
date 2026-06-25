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
