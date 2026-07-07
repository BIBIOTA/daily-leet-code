# String + Counting

### From: 1704. Determine if String Halves Are Alike (2026-07-07)

Input: s = "textbook"
Approach: 將字串切成前後兩半，分別計算各自的母音數量，比較是否相等。
Key insight: 只需要計算母音「數量」，不需要知道哪些母音——一個計數器就夠，不需要 Counter 或 Hash Table。

Trace (s = "textbook", mid = 4):
- front = "text" → 't','e','x','t' → 1 vowel ('e')
- back  = "book" → 'b','o','o','k' → 2 vowels ('o','o')
- 1 != 2 → False

Mistake I made: `front, back = s[mid:], s[:mid]`（前後對調）；`set('aeiou')` 未涵蓋大寫母音（應用 `char.lower()`）；`sum(a in vowels)` 對整個字串做 `in` 而非逐字元迭代。
