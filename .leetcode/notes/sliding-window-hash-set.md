# Sliding Window (Fixed Size) + Hash Set

固定大小視窗框住「索引距離」限制，視窗內容用 hash set 維護以 O(1) 判斷「值是否重複／存在」。

---

### From: 219. Contains Duplicate II (2026-08-27)

Input: `nums = [1, 2, 3, 1], k = 3` → `True`；`nums = [1, 2, 3, 1, 2, 3], k = 2` → `False`

Approach: 掃過 `nums`，維護一個「最近 k 個元素值」的 `set` 當作視窗。對每個 `i`：**先**查 `nums[i] in window`（命中代表前面 k 格內出現過同值 → `True`），**再**把 `nums[i]` 加入；當 `len(window) > k` 時移除 `nums[i-k]`（正要滑出距離範圍的最舊元素）。

Key insight: 「先查再加」保證命中的一定是某個 `j < i`（自己還沒進 set），索引必相異；移除的恰好是 `nums[i-k]`，因為 `set` 超過 k 個時，最舊元素索引就是 `i-k`，距離已到邊界。

Trace（`nums=[1,2,3,1], k=3`）:
- i=0 val=1: `1 in {}`? no → add → `{1}`；len 1 ≤ 3
- i=1 val=2: no → `{1,2}`；len 2 ≤ 3
- i=2 val=3: no → `{1,2,3}`；len 3 ≤ 3
- i=3 val=1: `1 in {1,2,3}`? **yes → return True**（索引 0 與 3，距離 3 ≤ k）

`k=0` 自然正確：每次加完 `len(window)=1 > 0` 立刻 `remove(nums[i])`，視窗永遠空 → 不可能命中。

```python
def containsNearbyDuplicate(nums, k):
    window = set()
    for i, num in enumerate(nums):
        if num in window:
            return True
        window.add(num)
        if len(window) > k:
            window.remove(nums[i - k])
    return False
```

複雜度：O(n) 時間（`in`/`add`/`remove` 平均 O(1)），O(min(n, k)) 空間。

Mistake I made:
- 初版只比對「剛好距離 k」的 `nums[i+k]` 與 `nums[i-k]`，漏掉距離 1..k-1 的配對（`[1,1,0,0], k=2` 回傳 False）。
- `i + k <= len(nums)` 讓 `nums[i+k]` 取到 `nums[len(nums)]` → IndexError（應 `<= len(nums) - 1`，或根本不該用這寫法）。
- 需 4 層 hint 才轉向「視窗 set + 先查再加 + 移除 nums[i-k]」的正解。
- 追問值差 ≤ t 變體（LC 220）答不出：`set` 只能精確比對，範圍查詢要改用寬度 `t+1` 的 bucket，或 `SortedList` 二分。
- pattern 只答「Sliding Window」，漏掉 Hash Set 組件（是它把回頭掃 k 格的 O(n·k) 降成 O(n)）。
