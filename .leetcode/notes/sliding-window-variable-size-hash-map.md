# Sliding Window (Variable Size) + Hash Map

## Pattern Summary

可變長度滑動視窗：左右指標各自移動，右指標每步擴展視窗，左指標在條件不滿足時收縮。用 Hash Map 記錄「字元最後出現的 index」，讓左邊界能直接跳到正確位置，而非逐步縮小。

---

### From: 3. Longest Substring Without Repeating Characters (2026-07-20)

Input: s = "dvdf" → Output: 3

Approach: 右指標 right 逐字掃描；char_index 記錄每個字元最後出現的 index；當 char_index[ch] >= left 時，左邊界直接跳到 char_index[ch] + 1；視窗大小為 right - left + 1。

Key insight: 當重複字元出現時，不是重置整個視窗，而是把左邊界移到「重複字元上次出現位置的後一格」。這樣視窗內所有字元依然唯一，且不會丟失其他合法字元。

Trace on "dvdf":
```
right=0, ch='d': not in char_index → char_index={d:0}, left=0, max=1
right=1, ch='v': not in char_index → char_index={d:0,v:1}, left=0, max=2
right=2, ch='d': char_index[d]=0 >= left=0 → left=1; char_index={d:2,v:1}, max=2
right=3, ch='f': not seen in window → char_index={d:2,v:1,f:3}, left=1, max=3
```

Mistake I made: 多次嘗試用計數（+/-1）或整個重置 dict 來處理重複字元，但這兩種方式都無法知道「重複發生在視窗哪個位置」。關鍵是改用 index tracking 而非 count tracking。

Guard condition `char_index[ch] >= left` 的用途：char_index 保留所有歷史記錄；若某字元的舊 index 已在 left 左側（視窗外），不能把 left 往左倒退——`>= left` 確保只在舊出現位置仍在視窗內時才移動左邊界。
