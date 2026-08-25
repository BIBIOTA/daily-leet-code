# Binary Search

## Pattern Summary

在「有序」或「半有序」陣列中，利用中間值的比較每次砍掉一半的搜尋範圍，達到 O(log n)。

核心骨架：
```
left, right = 0, len(nums) - 1
while left < right:
    mid = (left + right) // 2
    if <condition>:
        left = mid + 1   # mid 確定不是答案，跳過
    else:
        right = mid      # mid 可能是答案，保留
return nums[left]
```

---

### From: 153. Find Minimum in Rotated Sorted Array (2026-07-22)

Input: nums = [4, 5, 6, 7, 0, 1, 2]
Approach: 比較 nums[mid] 與 nums[right]。若 mid 比右端點大，斷點在右半邊，left = mid + 1；否則最小值在左半邊或就是 mid，right = mid。
Key insight: 不是找「mid 是否是最小值」，而是判斷「最小值在哪一半」，每次砍掉確定不含答案的半邊。

Trace（[4,5,6,7,0,1,2]）：
- left=0, right=6, mid=3 → nums[3]=7 > nums[6]=2 → left=4
- left=4, right=6, mid=5 → nums[5]=1 ≤ nums[6]=2 → right=5
- left=4, right=5, mid=4 → nums[4]=0 ≤ nums[5]=1 → right=4
- left=4, right=4 → return nums[4] = 0 ✅

Mistake I made: `left = mid` 而非 `left = mid + 1`，造成 left 沒有前進，陷入無窮迴圈（[2,1] 立刻復現）。另誤以為 pattern 是 Two Pointers，實為 Binary Search（left/right 是搜尋邊界，不是「雙向掃描」）。

---

### From: 153. Find Minimum in Rotated Sorted Array (2026-07-23) [Review]

Input: nums = [3, 4, 5, 1, 2]
Approach: 比較 nums[mid] 與 nums[right]。若 nums[mid] > nums[right]，斷點在右半，left = mid + 1；否則最小值在左半或就是 mid，right = mid。
Key insight: nums[right] 是穩定錨點——最小值永遠 ≤ nums[right]，所以用它比較能可靠判斷 mid 落在哪段。改用 nums[left] 在陣列未旋轉時會把最小值排除在搜尋範圍外。

Mistake I made: mid 連錯三次（nums[right]//2 → right//left 除零 → (right-left)//2 偏移量，正確應為 (left+right)//2）；指標移動用 +=1/-=1 而非跳到 mid/mid+1；return right 回傳索引應改為 nums[right]。

---

### From: 153. Find Minimum in Rotated Sorted Array (2026-08-26) [Review]

Input: nums = [4, 5, 6, 7, 0, 1, 2]
Approach: left/right/mid 框架與比較邏輯（nums[mid] vs nums[right]）都已內化寫對；唯一漏洞是最後 `return left` 忘記轉成 `return nums[left]`，回傳了索引而非數值。
Key insight: 迴圈跑完後 `left == right` 只是「答案的位置」，別忘了最後一步要用這個索引去陣列裡取值。

Mistake I made: `return left` 應為 `return nums[left]`（靠 /run 一次失敗抓出）。

Variant note（154 題重複元素）：若允許重複，`nums[mid] == nums[right]` 時無法判斷最小值在哪一半，需加 `elif nums[mid] == nums[right]: right -= 1` 安全縮小範圍，最壞情況退化為 O(n)。當時誤以為現有程式碼（沒有這個 elif 分支）已經能正確處理重複元素，用反例 `[1,1,1,0,1]`（現有程式碼回傳 1，正解應為 0）才釐清：`==` 情況目前是走進 `right = mid` 的 else 分支，會誤刪掉可能藏最小值的區域。
