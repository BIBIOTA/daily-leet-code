# Dynamic Programming

## From: 53. Maximum Subarray (2026-06-29)

Input: `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`
Approach: 維護「以當前元素結尾的最大子陣列和」(current) 與「全域最大」(best)，每步決定延伸或從頭重置。
Key insight: 重置條件是 `current < 0`（拖著負的前綴只會拉低總和），等價寫法：`current = max(current + num, num)`。

Trace（前幾步）:
```
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
current = -2, best = -2
num=1:  current = max(-2+1, 1) = 1,  best = 1
num=-3: current = max(1-3, -3) = -2, best = 1
num=4:  current = max(-2+4, 4) = 4,  best = 4
num=-1: current = max(4-1, -1) = 3,  best = 4
num=2:  current = max(3+2, 2) = 5,   best = 5
num=1:  current = max(5+1, 1) = 6,   best = 6  ← answer
```

DP 本質: `dp[i] = max(nums[i], dp[i-1] + nums[i])`，此解為空間壓縮版（O(1) space）。

Mistake I made: 重置條件寫成 `current + num < current`（等價 `num < 0`），導致遇到負數元素就重置，即使累積和仍為正；正確條件應為 `current + num < num`（等價 `current < 0`）。另外留下了永遠不會執行的 elif dead code。

---

## From: 53. Maximum Subarray (2026-07-01 複習)

Input: `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`
Approach: 同 Kadane's：`current += num`，再判斷是否 reset。最終寫法 `current += num; if current < num: current = num` 等價 `current = max(current + num, num)`。
Key insight: reset 的判斷條件跟 `best` 無關，只問「延伸後的和有沒有比只取 num 本身更差？」即 `current + num < num` → `current < 0`，而 `if current < num`（在 `+=` 之後）恰好等價於此。

Mistake I made: 試了 10+ 次不同 reset 條件（`current > now_sum`、`current < now_sum`、`current < best`、`current < num`（先比後延）等），混淆了「reset 門檻」與「更新 best 的門檻」，最終靠試錯而非推導找到正確邏輯。另外誤將此題 pattern 識別為 Sliding Window（視窗沒有固定端點，無法用雙指針維護）。

---

## From: 53. Maximum Subarray (2026-07-02 複習)

Input: `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`
Approach: 同 Kadane's：初始化 `current = max_sum = nums[0]`，從 `nums[1:]` 開始迭代；每步先 `current += num`，再判斷是否 reset（`if current < num: current = num`），最後更新 `max_sum`。
Key insight: reset 的比較對象是 `current`（當下累積和），不是 `max_sum`（全域最大）。`if current < num` 等價於「old current < 0」，即帶著負的前綴繼續延伸只會拉低總和。

Trace（關鍵步驟）:
```
[5, -8, 3, 2, 6]  ← 這個 case 暴露了錯誤的 reset 條件
current=5, max=5
num=-8: current=5-8=-3; -3 < -8? no → keep; max stays 5
num=3:  current=-3+3=0;  0 < 3? yes → reset current=3; max stays 5
num=2:  current=3+2=5;   5 < 2? no → keep; max stays 5
num=6:  current=5+6=11; 11 < 6? no → keep; max=11  ← correct
```

Mistake I made: reset 條件先後寫了兩個錯誤版本：
1. `if max_sum < num` → 只在 num 超越全域最大時才 reset，漏掉「累積和已為負但尚未超過 max_sum 的 num」的情況
2. 兩個 if 順序調換後同樣失敗——根本問題是比較對象錯誤
正確條件：`if current < num`（+=之後），與 max_sum 完全無關。另外留下冗餘 check `if max_sum < num`（因前一行已保證 `current >= num`，後面的 `if max_sum < current` 已涵蓋此情況）。

---

## From: 53. Maximum Subarray (2026-07-06 複習)

Input: `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`
Approach: 同 Kadane's：`current = max_sum = nums[0]`，從 `nums[1:]` 迭代；`current += num` 後若 `current < num` 則 reset；最後更新 `max_sum`。
Key insight: reset 條件 `if current < num`（`+=` 之後）等價於 `current = max(current + num, num)`——「延伸後的和比只取當前元素還差，就重新開始」。

Mistake I made: 無——首次乾淨通過，無 hint、無 run 失敗。

---

## From: 53. Maximum Subarray (2026-07-13 複習)

Input: `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`
Approach: 同 Kadane's：`last = max_count = nums[0]`，從 `nums[1:]` 迭代；`last = max(last + num, num)` 同時處理延伸與重置；最後更新 `max_count`。
Key insight: `max(last + num, num)` 一行等價於「若前綴和為負則重置」——等式兩邊相減即 `last < 0`，不需分開寫 if/else。

Mistake I made: 初始化 `max_count = last = 0`（應為 `nums[0]`），導致全負數陣列回傳 0；誤用 `range(nums[1:])` 而非直接迭代 `nums[1:]`。靠 3 次 /run 試錯修正。

---

## From: 53. Maximum Subarray (2026-07-17 複習)

Input: `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`
Approach: 同 Kadane's：`last_sum = max_sum = nums[0]`，從 index 1 起迴圈；`last_sum = max(last_sum + nums[i], nums[i])` 一行同時處理延伸與重置；最後更新 `max_sum`。
Key insight: 初始化必須用 `nums[0]` 而非 `0`——若初始為 0，全負數陣列時 `max_sum` 永遠不低於 0，回傳 0 而非正確的最大負值。

Mistake I made: 語法錯誤兩次——`range(1, nums)` 應為 `range(1, len(nums))`；`num[i]` 是拼錯，應為 `nums[i]`；靠 run 試錯 3 次才修正。時間/空間複雜度說反（O(n) time / O(1) space）。

---

## From: 53. Maximum Subarray (2026-07-20 複習)

Input: `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`
Approach: `sum_array = current = nums[0]`，從 index 1 起迴圈；`current += nums[i]` 後 `current = max(current, nums[i])`；最後更新 `sum_array`。
Key insight: 重置點是 `nums[i]` 而非 `0`——若用 `max(current, 0)`，全負數陣列時結果為 0，但題目要求至少選一個元素。

Trace（關鍵步驟）:
```
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
current = sum_array = -2
i=1: current=-2+1=-1 → max(-1,1)=1;  sum_array=1
i=2: current=1-3=-2  → max(-2,-3)=-2; sum_array=1
i=3: current=-2+4=2  → max(2,4)=4;   sum_array=4
i=4: current=4-1=3   → max(3,-1)=3;  sum_array=4
i=5: current=3+2=5   → max(5,2)=5;   sum_array=5
i=6: current=5+1=6   → max(6,1)=6;   sum_array=6  ← answer
```

Mistake I made: 無——首次乾淨複習通過（rung 0，run 失敗 0 次）。

---

## From: 53. Maximum Subarray (2026-09-03 複習)

Input: `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`
Approach: 初始化 `current = max_result = nums[0]`，從第二個元素開始掃描。對每個 `num`，以 `current = max(num, current + num)` 決定延伸現有子陣列或從此元素重新開始，再以 `max_result` 保留全域最佳值。
Key insight: 當前綴和為負時，帶著它加入 `num` 必定不如只從 `num` 開始；因此只需比較這兩種狀態，不需要 hash table。

Trace:
```
current = max_result = -2
num=1:  current=max(1, -2+1)=1;  max_result=1
num=-3: current=max(-3, 1-3)=-2; max_result=1
num=4:  current=max(4, -2+4)=4;  max_result=4
num=-1: current=max(-1, 4-1)=3;  max_result=4
num=2:  current=max(2, 3+2)=5;   max_result=5
num=1:  current=max(1, 5+1)=6;   max_result=6
```

Mistake I made: 初版以 `0` 初始化，會讓全負數陣列回傳錯誤值；接著曾只迭代 `nums[:1]`，並一度把 `+=` 放進 `max()` 的參數導致語法錯誤。最後也把模式誤認為 Hash Table。

---

## From: 198. House Robber (2026-07-06)

Input: `[2, 7, 9, 3, 1]`
Approach: 建立 dp 陣列，`dp[i]` 代表考慮到第 i 間為止的最大搶劫金額。base case：`dp[0]=nums[0]`，`dp[1]=max(nums[0],nums[1])`；轉移：`dp[i] = max(dp[i-1], dp[i-2] + nums[i])`。
Key insight: 對每間房子只有「偷」或「不偷」兩種選擇——偷就加上兩格前的最優值，不偷就繼承前一格的最優值。不需要窮舉所有非相鄰組合。

Trace:
```
nums = [2, 7, 9, 3, 1]
dp[0] = 2
dp[1] = max(2, 7) = 7
dp[2] = max(dp[1], dp[0]+9) = max(7, 11) = 11
dp[3] = max(dp[2], dp[1]+3) = max(11, 10) = 11
dp[4] = max(dp[3], dp[2]+1) = max(11, 12) = 12  ← answer
```

空間優化：因為 dp[i] 只依賴 dp[i-1] 和 dp[i-2]，可用兩個變數 prev2、prev1 滾動，降至 O(1) 空間。

Mistake I made: 初版用「奇偶分流」（偶數 index 一組、奇數 index 一組），錯誤假設最優解必是嚴格交替，無法處理 [2,1,1,2]→4 或 [5,1,1,5]→10 這類需跨兩格的情況。時間複雜度誤答 O(n log n)，實際為 O(n)。
