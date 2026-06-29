# Problem Log

| date | problem | pattern | result | hints_used | notes |
|------|---------|---------|--------|------------|-------|
| 2026-06-23 | #347 Top K Frequent Elements | heap / Counter | pass | rung 2 | Used Counter.most_common(k) |
| 2026-06-24 | #49 Group Anagrams | Hash Table | Passed | rung 2 | tuple(sorted(word)) as key; missed that str is also immutable in Python |
| 2026-06-24 | #1 Two Sum | Hash Table | Passed | rung 0 | defaultdict 換成 dict；修正 enumerate 用法；了解已排序陣列可改用 Two Pointers 達 O(1) 空間 |
| 2026-06-25 | #217 Contains Duplicate | Hash Table | Passed | rung 0 | len(set(nums)) != len(nums)；理解 O(1) space 替代方案需先 sort（O(n log n)） |
| 2026-06-26 | #121 Best Time to Buy and Sell Stock | Greedy / One Pass | Passed (partial) | rung 2 | float('inf') 初始化最低價；sell 與 last_min_price 獨立更新；space complexity 答錯（O(n) 應為 O(1)） |
| 2026-06-26 | #53. Maximum Subarray | Greedy / One Pass | Struggled | rung 4 | 初始化用 nums[0] 處理全負數；current 與 best 需獨立更新；max(current+num, num) 是重置的慣用寫法；O(n-1) 應寫為 O(n) |
| 2026-06-28 | #347. Top K Frequent Elements | Hash Table / Heap | Struggled | rung 4 | sorted() 語法錯誤（key 需為關鍵字參數）；空間複雜度誤答 O(1)，應為 O(n)；頻率表邏輯正確 |
| 2026-06-29 | #53. Maximum Subarray | Dynamic Programming (Kadane's) | Passed (partial) | rung 0 / run_failures 10 | 重置條件應為 current+num < num（等價 current < 0）；elif 分支為 dead code；靠 /run 試錯 10 次才找到正確邏輯 |
