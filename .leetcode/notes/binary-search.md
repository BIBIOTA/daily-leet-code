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
