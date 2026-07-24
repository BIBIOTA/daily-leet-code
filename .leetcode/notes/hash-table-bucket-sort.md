# Hash Table + Bucket Sort

### From: 347. Top K Frequent Elements (2026-07-21)

Input: nums = [1, 1, 1, 2, 2, 3], k = 2
Approach: 先用 Hash Table 統計每個元素的頻率，再建立 n+1 個桶（index = 頻率），最後從高頻桶往低頻桶掃，收集到 k 個即回傳。
Key insight: 頻率的上限是 n（陣列長度），因此可以「用頻率當 index」直接放桶，不需排序，達成 O(n)。

Trace (nums = [1,1,1,2,2,3], k=2):
1. freq = {1:3, 2:2, 3:1}
2. buckets[3]=[1], buckets[2]=[2], buckets[1]=[3]
3. 從 i=6 往下掃 → i=3 取出 1 → i=2 取出 2 → len==k，return [1, 2]

Mistake I made: `for num, count in freq` 迭代 dict 只給 key，需改為 `freq.items()` 才能拿到 (key, value)。另外 result 未初始化就使用（NameError）。if check 應放在內層 loop 裡（每加一個元素就判斷），而非放在外層（整桶處理完才判斷）——本題因答案唯一保證不影響結果，但嚴謹版應在內層。

### From: 347. Top K Frequent Elements (2026-07-22) — Review

Input: nums = [1, 1, 1, 2, 2, 3], k = 2
Approach: Counter 統計頻率 → n+1 個桶（index = 頻率）→ 從高頻桶往低頻掃，累積到 k 個回傳。
Key insight: 頻率最大值 = n，所以桶必須是 n+1 個（index 0 到 n），建 n 個就會在 count=n 時 IndexError。

Trace (nums = [5,5,5,5], k=1 — the breaking case):
- Counter: {5: 4}，count=4
- buckets = [[] for _ in range(4)]  →  索引 0~3，無索引 4  →  IndexError ✗
- buckets = [[] for _ in range(5)]  →  索引 0~4，buckets[4]=[5]  →  OK ✓

Mistake I made:
- `for num, count in nums_count` → 忘記 `.items()`，Counter 直接迭代只給 key
- `if in buckets[i]:` → 語法錯誤，應為 `if buckets[i]:`
- `range(len(buckets), 0, -1)` → 起點 len(buckets) 越界，應為 `range(len(buckets)-1, 0, -1)`
- `buckets = [[] for _ in nums]` → 只建 n 個桶，應為 `range(len(nums) + 1)` 才有索引 0~n

### From: 347. Top K Frequent Elements (2026-07-23) — Review

Input: nums = [1, 1, 1, 2, 2, 3], k = 2
Approach: Counter 統計頻率 → n+1 個桶（index = 頻率）→ 從高頻桶往低頻掃，累積 k 個後立即 `return results`。
Key insight: `break` 只跳出內層 `for num in buckets[i]`，外層 `for i in range(...)` 仍繼續；改用 `return results` 才能一次終止兩層迴圈。

Trace (nums = [1,1,1,2,2,3], k=2 — the break-only bug):
- i=3: append 1, len=1
- i=2: append 2, len=2, break inner → 外層繼續
- i=1: append 3! len=3 ≠ k → return [1, 2, 3]  ✗
- 改為 `if len(results)==k: return results` → i=2 直接 return [1, 2]  ✓

Mistake I made:
- `range(len(nums)) + 1` → range 物件不能 +1，應為 `range(len(nums) + 1)`
- `range(len(buckets), 0, -1)` → 起點再次越界，應為 `range(len(buckets)-1, 0, -1)`
- `return nums[k]` / `return nums[k-1]` → 回傳單一 int 而非 list；當 len(nums)==k 時應 `return list(nums)` 或直接讓主邏輯處理
- `else: break` → 只跳內層，改 `if len==k: return results` 才能雙層同時終止

### From: 347. Top K Frequent Elements (2026-07-24) — Review

Input: nums = [1, 1, 1, 2, 2, 3], k = 2
Approach: Counter 統計頻率 → n+1 個桶（index = 頻率）→ 從高頻桶往低頻掃，累積 k 個後立即 return results。
Key insight: 頻率上限為 n（不是輸入值的範圍），所以頻率可直接當 index；這是 O(n) 的前提。直接迭代 Counter 只給 key，需 `.items()` 才能同時拿 (key, value)。

Trace (nums = [1,1,1,2,2,3], k=2):
1. nums_count = {1:3, 2:2, 3:1}
2. buckets 長度 7（= len(nums)+1 = 6+1）
3. buckets[3]=[1], buckets[2]=[2], buckets[1]=[3]
4. i=6,5,4: 空。i=3: append 1 → [1]。i=2: append 2 → [1,2]，len==k → return [1,2]

Mistake I made:
- `from collection import Counter`（連兩次）→ 模組名是 `collections`（有 s）
- `range(nums + 1)` → nums 是 list，不能加 int；應為 `range(len(nums) + 1)`
- `for num, count in nums_count` → 需改為 `nums_count.items()` 才能解包 (key, value)
- 最後一行 `return results`（迴圈外）是 dead code：題目保證 k ≤ 唯一元素數，inner return 一定先觸發
