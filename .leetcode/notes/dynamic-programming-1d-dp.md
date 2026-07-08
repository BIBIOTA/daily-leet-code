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
