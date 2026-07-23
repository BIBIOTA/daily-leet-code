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

---

### From: 3. Longest Substring Without Repeating Characters — Set 版本 (2026-07-23)

Input: s = "abcabcbb" → Output: 3

Approach: 維護 set 記錄視窗內的字元；右指標逐字推進，若 s[right] 已在 set 中，用 while 迴圈從左逐步移除直到重複消失；之後才 add s[right]；全程以 max_len 追蹤最大視窗。

Key insight: `s[right]` 的 add 必須在 while 迴圈**外面**。放在裡面會讓 while 條件永遠成立，導致 left 越界崩潰。

Trace on "abcabcbb":
```
right=0 ('a'): not in {} → add → {a}, max=1
right=1 ('b'): not in {a} → add → {a,b}, max=2
right=2 ('c'): not in {a,b} → add → {a,b,c}, max=3
right=3 ('a'): in {a,b,c} → while: remove s[0]='a'→{b,c},left=1; 'a' not in {b,c} → add → {b,c,a}, max=3
right=4 ('b'): in {b,c,a} → while: remove s[1]='b'→{c,a},left=2; add → {c,a,b}, max=3
...
```

Mistake I made: 把 `substring.add(s[right])` 放進 while 迴圈內，加完後 while 條件仍成立（自己剛加的）→ 無限縮左直到 left 越界（KeyError）。另外 `max_len` 從未更新，最後 `return len(substring)` 只是最終視窗大小，不是歷史最大值。
