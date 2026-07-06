# Sliding Window (Fixed Size)

### From: 643. Maximum Average Subarray I (2026-07-06)

Input: nums = [1, 12, -5, -6, 50, 3], k = 4
Approach: 先計算前 k 個元素的總和作為初始 window，再從 index k 開始往右滑，每次加入右側新元素、移除左側舊元素，追蹤最大總和，最後除以 k 回傳平均值。
Key insight: window 每次移動只需「加一減一」，避免重複加總，將 O(n·k) 降為 O(n)。

Trace (k=4):
- 初始: sum([1,12,-5,-6]) = 2, max_sum = 2
- i=4: 2 + 50 - 1 = 51, max_sum = 51
- i=5: 51 + 3 - 12 = 42, max_sum = 51
- 回傳 51 / 4 = 12.75

Mistake I made: range 上界寫成 `len(nums) - 1`，漏掉最後一個 window；range 右界本身就是 exclusive，不需再 -1。另外誤用 Counter.most_common(k) 取最高頻元素，與「連續子陣列」概念無關。

### From: 1456. Maximum Number of Vowels in a Substring of Given Length (2026-07-06)

Input: s = "abciiidef", k = 3
Approach: 先計算前 k 個字元的母音數作為初始計數，再滑動窗口：每步用 s[i-k] 判斷離開字元（若為母音則 -1），用 s[i] 判斷進入字元（若為母音則 +1），同時追蹤歷史最大值。
Key insight: 離開窗口的字元直接用 `s[i - k]` 取得，不需要維護額外的 window 字串，空間從 O(k) 降至 O(1)。

Trace (k=3):
- 初始: "abc" → 1 個母音 (a)，last_count=1, max_count=1
- i=3 (s[i]='i', s[i-k]='a'): 'a' 出 → -1=0；'i' 入 → +1=1；max=1
- i=4 (s[i]='i', s[i-k]='b'): 'b' 出 → 0；'i' 入 → +1=2；max=2
- i=5 (s[i]='i', s[i-k]='c'): 'c' 出 → 0；'i' 入 → +1=3；max=3
- i=6 (s[i]='d', s[i-k]='i'): 'i' 出 → -1=2；'d' 入 → 0；max=3

Mistake I made: 混淆 current_count 與 max_count，把 max_count 當做 window_count 的初始值，導致歷史最大值「污染」後續計算；應保持兩個獨立變數。另外 set('a','e','i','o','u') 語法錯誤，正確為 set("aeiou")。
