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

---

### From: 53. Maximum Subarray (2026-06-26)

Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Approach: 一次掃過陣列，維護「以當前元素結尾的最大子陣列和（current）」與「歷史最大值（best）」，兩個變數各自獨立更新。
Key insight: 每一步用 `max(current + num, num)` 決定是否重新開始——若累積和已拖累當前元素，就從當前元素重新起步；`best` 永遠在 `current` 更新後無條件取最大。

```
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
current=-2, best=-2
num=1:  current=max(-1,1)=1,   best=max(-2,1)=1
num=-3: current=max(-2,-3)=-2, best=max(1,-2)=1
num=4:  current=max(2,4)=4,    best=max(1,4)=4
num=-1: current=max(3,-1)=3,   best=max(4,3)=4
num=2:  current=max(5,2)=5,    best=max(4,5)=5
num=1:  current=max(6,1)=6,    best=max(5,6)=6  ✅
num=-5: current=max(1,-5)=1,   best=max(6,1)=6
num=4:  current=max(5,4)=5,    best=max(6,5)=6
```

Mistake I made:
- 初始化 `best = 0` → 全負數輸入時永遠回傳 0，應改為 `best = nums[0]`
- 用 `if/elif` 把 `current` 和 `best` 的更新綁在一起 → 兩者必須完全獨立，先更新 `current` 再更新 `best`
- Big-O 寫成 `O(n-1)`，常數項應捨去，正確寫法是 `O(n)`
