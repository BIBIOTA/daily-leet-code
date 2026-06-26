# Problem Log

| date | problem | pattern | result | hints_used | notes |
|------|---------|---------|--------|------------|-------|
| 2026-06-23 | #347 Top K Frequent Elements | heap / Counter | pass | rung 2 | Used Counter.most_common(k) |
| 2026-06-24 | #49 Group Anagrams | Hash Table | Passed | rung 2 | tuple(sorted(word)) as key; missed that str is also immutable in Python |
| 2026-06-24 | #1 Two Sum | Hash Table | Passed | rung 0 | defaultdict 換成 dict；修正 enumerate 用法；了解已排序陣列可改用 Two Pointers 達 O(1) 空間 |
| 2026-06-25 | #217 Contains Duplicate | Hash Table | Passed | rung 0 | len(set(nums)) != len(nums)；理解 O(1) space 替代方案需先 sort（O(n log n)） |
| 2026-06-26 | #121 Best Time to Buy and Sell Stock | Greedy / One Pass | Passed (partial) | rung 2 | float('inf') 初始化最低價；sell 與 last_min_price 獨立更新；space complexity 答錯（O(n) 應為 O(1)） |
