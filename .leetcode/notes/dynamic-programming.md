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
