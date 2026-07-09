# Heap / Counter 筆記

## 核心模板

```python
from collections import Counter

Counter(nums).most_common(k)  # 直接取前 k 個最高頻元素，回傳 [(元素, 次數), ...]
```

## 實例：#347 Top K Frequent Elements

```python
from collections import Counter

def topKFrequent(nums, k):
    counter_nums = Counter(nums).most_common(k)
    return [num for num, _ in counter_nums]
```

`Counter([1,1,1,2,2,3]).most_common(2)` → `[(1, 3), (2, 2)]`

## 複雜度

- 時間：O(n log k)，most_common 內部用 heap，只維護 k 個元素
- 空間：O(n)，Counter 存所有 unique 元素

vs. `sorted()` 全排序是 O(n log n)，k 遠小於 n 時 most_common 明顯較快

## 何時用

- 找「最高頻的 k 個元素」
- 需要頻率統計 + 排序取前 k

---

### From: 347. Top K Frequent Elements（2026-06-28 複習）

Input: nums = [1, 1, 1, 2, 2, 3], k = 2
Approach: 用 dict 手動建頻率表，再用 sorted(freq.items(), key=lambda x: x[1], reverse=True)[:k] 取前 k 名
Key insight: sorted() 的 key 必須是關鍵字參數；sorted(freq.items()) 排序的是 (key, value) tuple，不是 dict 本身

Mistake I made: 空間複雜度誤答 O(1)——只要建了 dict / Counter 就是 O(n)，因為儲存了所有 unique 元素；sorted() 語法混淆（把 key 當位置參數傳入）

---

### From: 347. Top K Frequent Elements（2026-06-29 複習）

Input: nums = [1, 1, 1, 2, 2, 3], k = 2
Approach: Counter(nums).most_common(k) 直接取前 k 個最高頻元素，再 list comprehension 取 num
Key insight: most_common(k) 底層是 min-heap，時間 O(n log k)；若改用 sorted() 全排序則退化為 O(n log n)，違反 follow-up 要求

Trace（Counter 內部流程）:
- Counter([1,1,1,2,2,3]) → {1: 3, 2: 2, 3: 1}
- most_common(2) 維護大小為 2 的 min-heap，遍歷每個元素：push → 超過 k 就 pop 最小
- 結果：[(1, 3), (2, 2)] → return [1, 2]

Mistake I made: import 語法錯誤寫成 `import collections from Counter`（Python 正確語法為 `from collections import Counter`）；說明 alternative 時選了 sorted()，忘記這樣複雜度是 O(n log n)，應改為手動維護 min-heap 才能保持 O(n log k)

---

### From: 347. Top K Frequent Elements（2026-06-30 複習）

Input: nums = [1, 1, 1, 2, 2, 3], k = 2
Approach: Counter(nums).most_common(k) 取前 k 高頻，list comprehension `[num for num, _ in frequent_k]` 解構 tuple 取出數字
Key insight: most_common(k) 回傳的是 **list of tuples**，不是 dict — 不能呼叫 `.values()`，要直接 unpack

Mistake I made: 三次對 list 呼叫 `.values()`（只有 dict 才有此方法）；空間複雜度誤答 O(n·k)，應為 O(n)——Counter 最多存 n 個 unique 元素，output 存 k 個，合計 O(n+k) = O(n)

---

### From: 347. Top K Frequent Elements（2026-07-03 複習）

Input: nums = [1, 1, 1, 2, 2, 3], k = 2
Approach: Counter(nums).most_common(k) 取前 k 高頻，`[num for num, _ in result]` 解構 tuple 取出數字
Key insight: most_common(k) 回傳 list of tuples，不能呼叫 .keys()；整體 O(n log k)，空間 O(n)

Mistake I made: 首次嘗試對 most_common 結果呼叫 `.keys()`（list 沒有此方法）；空間複雜度誤答 O(n·k)，實際上 Counter 存 n 個元素、output 存 k 個，合計 O(n)

---

### From: 347. Top K Frequent Elements（2026-07-09 複習）

Input: nums = [1, 1, 1, 2, 2, 3], k = 2
Approach: Counter(nums).most_common(k) 取前 k 高頻，`[num for num, _ in frequent_k]` 解構 tuple 取數字
Key insight: most_common(k) 底層是 `heapq.nlargest(k, ...)`，會遍歷「所有相異元素 u」逐一與大小為 k 的 heap 比較 → 這段是 **O(u log k)**，最壞 u=n 時 O(n log k)。log 的乘數是「相異元素數 u」不是 k！

複雜度直覺（本輪追問的重點）:
- k 只決定「每次 heap 操作多貴」（heap 高度 → log k）
- u（相異元素數）決定「操作做幾次」（每個相異元素都要比一次）
- 所以是 u·log k，不是 k·log k；例如 n=100000 全相異、k=3 → heap 操作跑 100000 次而非 3 次

Mistake I made: 時間複雜度誤答 O(n + k log k)，正解 O(n + u log k)；誤以為 heap 操作只跑 k 次；pattern 只答 Hash Table，漏了 Heap / Top-K selection 這一半（統計用 hash、取前 k 用 heap 或 bucket sort）
