# Dynamic Programming (1D DP)

## Pattern Summary

用一維 DP 陣列（或壓縮成滾動變數）記錄「到第 i 個元素為止的最優解」，每步依賴前幾個狀態。

---

### From: 198. House Robber (2026-07-07)

Input: nums = [2, 7, 9, 3, 1]
Approach: 滾動兩個變數 prev_2、prev_1，每間房子選「搶（prev_2 + nums[i]）」或「不搶（prev_1）」取較大值，往右掃一次。
Key insight: 只需要「前兩間」的狀態，不需要完整 dp 陣列，壓縮成兩個整數即可達到 O(1) 空間。

Trace（nums = [2, 7, 9, 3, 1]）：
```
i=0: num=2, current=max(0, 0+2)=2,  prev_2=0, prev_1=2
i=1: num=7, current=max(2, 0+7)=7,  prev_2=2, prev_1=7
i=2: num=9, current=max(7, 2+9)=11, prev_2=7, prev_1=11
i=3: num=3, current=max(11,7+3)=11, prev_2=11, prev_1=11
i=4: num=1, current=max(11,11+1)=12,prev_2=11, prev_1=12
return 12
```

Mistake I made: 用 dict 當作 prev_1/prev_2，導致無法對 dict 做加法；正確做法是用兩個整數初始化為 0。

---

### From: 198. House Robber — Review (2026-07-08)

Input: nums = [1, 2, 3, 1]
Approach: 滾動兩個變數 prev_2、prev_1，每步取「搶這棟（prev_2 + nums[i]）」vs「跳過（prev_1）」較大值；shift 時先存舊 prev_1 再更新，或用 tuple 同步賦值避免順序問題。
Key insight: prev_2 必須在 prev_1 被覆寫之前存起來，否則「前兩步」的距離會被壓縮成零，導致答案偏大。

Trace（nums = [1, 2, 3, 1]）：
```
i=0: current=max(0+1, 0)=1,  prev_2←0,  prev_1←1
i=1: current=max(0+2, 1)=2,  prev_2←1,  prev_1←2
i=2: current=max(1+3, 2)=4,  prev_2←2,  prev_1←4
i=3: current=max(2+1, 4)=4,  prev_2←4,  prev_1←4
return 4 ✓
```

最簡寫法（tuple 同步賦值，天然解決順序問題）：
```python
prev_2, prev_1 = 0, 0
for num in nums:
    prev_2, prev_1 = prev_1, max(prev_1, prev_2 + num)
return prev_1
```

Mistake I made: 用 if/else 交替更新 prev_1 和 prev_2，每輪只有一個變數被更新，且 prev_2 拿到的是已更新的 prev_1 而非舊值，導致連續三次嘗試答案都偏大。

---

### From: 198. House Robber — Review (2026-07-09) ✅ 首次乾淨通過

Input: nums = [1, 2, 3, 1]
Approach: 滾動兩個變數，迴圈中 `current = num + prev_2`，再 `prev_2 = prev_1`、`prev_1 = max(current, prev_1)`——先把舊 prev_1 存進 prev_2，再更新 prev_1，順序正確就不會踩到之前的 shift bug。
Key insight: 決定「搶這間」時上一間必須跳過，只能接續「前兩間」的最佳解 prev_2；`max(current, prev_1)` 就是「搶 vs 不搶」的抉擇。這正是 dp[i] = max(dp[i-1], dp[i-2] + nums[i]) 的滾動版。

零提示、零 run 失敗，時間 O(n) / 空間 O(1) 皆答對。相較 2026-07-07（rung 4）與 2026-07-08（rung 3 + 6 次 run 失敗）明顯進步——之前反覆卡的 shift 順序這次一次寫對。

Mistake I made: 無。

---

### From: 198. House Robber — Review (2026-07-11)

Input: nums = [2, 1, 1, 2]
Approach: 滾動兩個變數 prev、curr，用 Python tuple unpacking 同步賦值：`prev, curr = curr, max(curr, num + prev)`，掃一次陣列。
Key insight: tuple unpacking 右側全部先計算完才賦值，天然解決「shift 前後順序」問題，不需要 `current` 暫存變數。

Trace（nums = [2, 1, 1, 2]）：
```
初始: prev=0, curr=0
num=2: prev=0, curr=max(0, 2+0)=2
num=1: prev=2, curr=max(2, 1+0)=2    ← 這裡 prev 用的是舊的 curr(0) → 不對
```
⚠️ 注意：`prev, curr = curr, max(curr, num + prev)` 右側 `num + prev` 的 `prev` 是舊值（更新前），Python 右側整體先算，所以：
```
num=2: prev←0, curr←max(0,2+0)=2
num=1: prev←2, curr←max(2,1+0)=2
num=1: prev←2, curr←max(2,1+2)=3
num=2: prev←3, curr←max(3,2+2)=4
return 4 ✓
```

Mistake I made: 初版寫 `prev_1 = current`（沒有 max），強制每間房都搶，忽略跳過當間更優的情況，導致 [2,1,1,2] 答 3 而非 4。

---

### From: 198. House Robber — Review (2026-07-16)

Input: nums = [1, 2, 3, 1]
Approach: 滾動兩個變數，先 `prev_2 = prev_1`（保存舊值），再 `prev_1 = max(curr, prev_2)`（比較搶 vs 不搶）。
Key insight: update 順序是唯一雷點——若先更新 prev_1 再 shift prev_2，prev_2 每輪都等於最新的 prev_1，「跳一間」的距離消失，答案變成全部加總。想避免順序 bug 可改用 tuple unpacking：`prev, curr = curr, max(curr, num + prev)`。

Mistake I made: 第一次把 `prev_1 = max(curr, prev_2)` 放在 `prev_2 = prev_1` 之前，一次 run 失敗後自行識別並修正順序。

---

### From: 198. House Robber — Review (2026-07-24)

Input: nums = [1, 2, 3, 1]
Approach: 先算 `curr = nums[i] + prev_2`，再 `prev_2 = prev_1`，最後 `prev_1 = max(prev_1, curr)`——三行順序不能對調。
Key insight: `prev_2 = prev_1` 必須在 `prev_1` 更新**之後**執行，才能讓 prev_2 持有舊的 prev_1；反過來先 shift 再計算，prev_2 與 prev_1 相等，「跳一間」的距離消失。

⚠️ 第三次犯同類型錯誤（前兩次：2026-07-08 的 if/else 分支錯誤、2026-07-16 的更新順序對調）。建議預設用 tuple unpacking：
```python
prev_2, prev_1 = 0, 0
for num in nums:
    prev_2, prev_1 = prev_1, max(prev_1, prev_2 + num)
return prev_1
```
Python 右側整體先求值，天然防止 shift 順序 bug。

Mistake I made: 連續三次嘗試都是代入順序錯誤——先執行 `prev_2 = prev_1` 後，`prev_2` 已等於最新 `prev_1`，再用 `prev_2` 計算等同把相鄰兩間同時搶。
