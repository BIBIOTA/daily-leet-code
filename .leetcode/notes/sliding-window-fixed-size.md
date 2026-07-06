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
