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
| 2026-06-29 | #49. Group Anagrams | Hash Table | Passed (partial) | rung 3 | return 語法混淆（多餘的 []）；時間複雜度誤答 O(n)，應為 O(n·k log k) |
| 2026-06-29 | #1. Two Sum | Hash Table | Struggled | rung 0 | `result.keys()` 多餘（直接 `if diff in result` 即可）；`else` 分支可刪；code quality partial；正確識別 sorted array 可改用 Two Pointers 省至 O(1) 空間 |
| 2026-06-29 | #217 Contains Duplicate | Hash Table | Struggled | rung 0 | 空間複雜度誤答 O(1)，應為 O(n)；set() 建立最多 n 個元素的額外空間 |
| 2026-06-29 | #121. Best Time to Buy and Sell Stock | Greedy / One Pass | Passed (partial) | rung 1 | 多餘的 max_price 追蹤造成條件/賦值不一致；移除後簡化為 min_price + price - min_price 直接計算；初始化拼寫 price[0] 應為 prices[0] |
| 2026-06-29 | #347. Top K Frequent Elements | Hash Table + Heap (Top K Elements) | Struggled | rung 0 | import 語法錯誤（import collections from Counter）；alternative 直覺用 sorted() O(n log n) 而非手動 heap O(n log k)；不確定 pattern 名稱 |
| 2026-06-30 | #347. Top K Frequent Elements | Hash Table + Heap | Passed (partial) | rung 0 | 對 list 呼叫 .values() 錯誤（run 失敗 3 次）；空間複雜度誤答 O(n·k)，應為 O(n) |
| 2026-06-30 | #49. Group Anagrams | Hash Table | Struggled | rung 0 | return 語法連錯三次（list comprehension 誤用、dict_values 包裝錯誤、語法錯誤）；時間複雜度誤答 O(n log k)，應為 O(n·m log m)；空間複雜度誤答 O(n)，應為 O(n·m) |
| 2026-06-30 | #1. Two Sum | Hash Table | Passed | rung 0 | 乾淨解出；complement lookup 模式掌握；正確說明 sorted array 可改用 Two Pointers O(1) 空間 |
| 2026-06-30 | #217. Contains Duplicate | Hash Table | Passed | rung 0 | 乾淨解出；正確分析 O(n) 時間 / O(n) 空間；理解 O(1) 空間替代方案需先 sort |
| 2026-07-01 | #53. Maximum Subarray | Dynamic Programming (Kadane's) | Passed (partial) | rung 0 / run_failures 11 | reset 條件 current < num 等價 max(current+num, num)；run 試錯 11 次才找到正確邏輯；Sliding Window 誤識 pattern，應為 DP / Kadane's |
| 2026-07-01 | #49. Group Anagrams | Hash Table + Canonical Form | Passed | rung 0 | 乾淨解出；正確分析時間 O(n·k log k) 空間 O(n·k)；了解改用 26-element freq tuple 可優化至 O(n·k) |
| 2026-07-02 | #121. Best Time to Buy and Sell Stock | Greedy / One Pass | Struggled | rung 0 | 變數命名混淆（best_price 追蹤賣價而非利潤）；run_failures 3 次；dead code (if max_profit < 0 guard) |
| 2026-07-02 | #53. Maximum Subarray | Dynamic Programming (Kadane's) | Passed (partial) | rung 0 / run_failures 3 | reset 條件 `current < num`（after +=）等價 `max(current+num, num)`；有冗餘 check `if max_sum < num`（可刪）；靠 run 試錯 3 次修正重置條件；pattern 誤答 Greedy，應為 DP / Kadane's |
| 2026-07-03 | #1. Two Sum | Hash Table | Passed | rung 0 | 乾淨複習通過；正確說明排序陣列可改用 Two Pointers 達 O(1) 空間 |
| 2026-07-03 | #217. Contains Duplicate | Hash Table | Passed | rung 0 | typo (nuns→nums) 靠 /run 發現；時間複雜度誤答 O(n log n)，實際為 O(n)；set() 是 hash table，平均 O(1) 插入 |
| 2026-07-03 | #121. Best Time to Buy and Sell Stock | Greedy / One Pass | Passed | rung 0 | `min_price = max(...)` 誤寫為 min，靠 /run 發現；空間複雜度誤答 O(n)，應為 O(1)；理解順序對調不影響正確性 |
| 2026-07-03 | #347. Top K Frequent Elements | Hash Table + Heap | Passed | rung 0 | 首次用 .keys() 呼叫 list 導致 AttributeError；空間複雜度誤答 O(n·k)，應為 O(n)；pattern 誤識為 Hash Table，應為 Hash Table + Heap |
| 2026-07-03 | #49. Group Anagrams | Hash Table + Canonical Form | Passed | rung 0 | 複習乾淨通過；時間複雜度誤答 O(n log k)，應為 O(n·k log k)；了解字母頻率 tuple 可優化至 O(n·k) |
| 2026-07-06 | #53. Maximum Subarray | Dynamic Programming (Kadane's) | Passed | rung 0 | 首次乾淨複習通過；正確識別 pattern 為 DP / Kadane's；理解 `max(current+num, num)` 等價慣用寫法；了解分治法時間複雜度 O(n log n) |
| 2026-07-06 | #121. Best Time to Buy and Sell Stock | Greedy / One Pass | Passed | rung 0 | 乾淨複習通過；正確分析 O(n) 時間 / O(1) 空間；理解 variant 多次交易需改用 Greedy 累加相鄰正差值；pattern 誤識為 Dynamic Programming，應為 Greedy / One Pass |
| 2026-07-06 | 198. House Robber | Dynamic Programming (1D DP) | Passed (partial) | rung 5 | 時間複雜度誤答 O(n log n)，應為 O(n)；run 失敗 5 次；需 5 層 hint 才完成；空間可優化至 O(1) 使用滾動變數 |
| 2026-07-06 | 643. Maximum Average Subarray I | Sliding Window (Fixed Size) | Passed (partial) | rung 4 | Counter.most_common 誤用；range off-by-one（len-1 → len）；dead code Counter import；用 4 層 hint 完成 |
| 2026-07-06 | 1456. Maximum Number of Vowels in a Substring of Given Length | Sliding Window (Fixed Size) | Passed (partial) | rung 1 | set('a','e',...) 語法錯誤（應為 set("aeiou")）；未分離 current_count 與 max_count 造成多次 bug；靠 run 試錯 8 次定位正確邏輯；最終理解 s[i-k] 取離開字元可省略 k_vowels 字串 |
| 2026-07-06 | 567. Permutation in String | Sliding Window (Fixed Size) | Passed (partial) | rung 4 | 誤用 tuple/sorted 枚舉排列；true/false 大小寫錯誤；需 4 層 hint 才轉向 Counter 頻率比較；時間複雜度誤答 O(K log n)，應為 O(n)；空間複雜度誤答 O(n)，應為 O(1) |
| 2026-07-07 | 49. Group Anagrams | Hash Table + Canonical Form | Struggled | rung 0 | 缺少 defaultdict import（NameError）；時間複雜度誤答 O(n·k)，應為 O(n·k log k)；了解字元計數陣列可優化至 O(n·k) |
