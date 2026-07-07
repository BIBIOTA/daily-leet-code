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

### From: 643. Maximum Average Subarray I (2026-07-07) — 複習

Input: nums = [1, 12, -5, -6, 50, 3], k = 4
Approach: 計算前 k 元素初始總和，從 index k 起滑動窗口（+右入 -左出），追蹤最大總和，最後除以 k。
Key insight: 所有子陣列長度相同（都是 k），因此「最大平均值 ≡ 最大總和」——只需找 sum，不需在每步除以 k。

Mistake I made: 無（複習乾淨通過）

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

### From: 567. Permutation in String (2026-07-06)

Input: s1 = "ab", s2 = "eidbaooo"
Approach: 建立 s1 的 Counter 頻率表，再對 s2 維護一個長度固定為 len(s1) 的 Counter 窗口；每次右進一字 +1、左出一字 -1，計數歸零時 del 該 key，每步比較兩個 Counter 是否相等。
Key insight: 排列的本質是「字母頻率相同」，不需枚舉所有排列——固定長度窗口 + Counter 比較即可，且兩個 Counter 比較是 O(26) = O(1)。

Trace (s1="ab", window 滑過 s2="eidbaooo"):
- 初始 win: {'e':1,'i':1} ≠ s1c {'a':1,'b':1}
- i=2 (進'd', 出'e'): win={'i':1,'d':1} ≠ s1c
- i=3 (進'b', 出'i'): win={'d':1,'b':1} ≠ s1c
- i=4 (進'a', 出'd'): win={'b':1,'a':1} == s1c → True

Mistake I made: 用 sorted(s1, reverse=True) 只生成一種排列，誤以為枚舉幾個代表即可；用 tuple(s2) 後嘗試用 string in tuple，型別完全不對。應從「比較頻率」而非「列舉排列」的角度思考。
