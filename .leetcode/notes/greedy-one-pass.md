# Greedy / One Pass

### From: 121. Best Time to Buy and Sell Stock (2026-06-26)

Input: prices = [7, 1, 5, 3, 6, 4]
Approach: 一次掃過陣列，同時維護「到目前為止的最低買入價」與「到目前為止的最大利潤」，兩個變數各自獨立更新。
Key insight: 對每個賣出日，最佳買入點永遠是它之前的歷史最低價——不需要暴力嘗試所有組合。

```
price=7: min=7, profit=0
price=1: min=1, profit=0   ← 更新最低價
price=5: min=1, profit=4   ← 5-1=4
price=3: min=1, profit=4   ← 3-1=2 < 4，不更新
price=6: min=1, profit=5   ← 6-1=5 ✅
price=4: min=1, profit=5   ← 4-1=3 < 5，不更新
```

Mistake I made:
- `last = price` 放在每次迴圈末尾 → 變成「上一個價格」而非「歷史最低價」，兩者不同
- `int('inf')` 不合法，Python 無限大要用 `float('inf')`
- Space complexity 答成 O(n)，實際上只用兩個變數，是 O(1)
