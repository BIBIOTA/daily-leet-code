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
