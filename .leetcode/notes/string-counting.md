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

### From: 1704. Determine if String Halves Are Alike (2026-07-11) — 複習 2

Input: s = "AaEeIiOoUu"
Approach: 切成前後兩半，用 `set('aeiouAEIOU')` 涵蓋大小寫，`sum(c in vowels for c in half)` 分別計數，比較相等。
Key insight: 母音 set 必須涵蓋大小寫；Python 字串切片（`s[:mid]`）建立副本，嚴格 O(1) 空間需改用 index 迭代。

Trace (s = "AaEeIiOoUu", mid = 5):
- front = "AaEeI" → A,a,E,e,I → 5 vowels
- back  = "iOoUu" → i,O,o,U,u → 5 vowels
- 5 == 5 → True

Mistake I made: 初版 `set('aeiou')` 漏大寫母音，edge case `"AaEeIiOoUu"` 揭露（應回傳 True 卻得 False）；空間複雜度誤答 O(1)，切片 `s[:mid]` 和 `s[mid:]` 各建 O(n/2) 副本，正確應為 O(n)。

### From: 1704. Determine if String Halves Are Alike (2026-07-08) — 複習

Input: s = "book"
Approach: 切成前後兩半（各 `len//2` 個字元），用 `sum(c in vowels for c in half)` 分別計數，比較是否相等。
Key insight: 母音 set 必須同時包含大小寫（`set('aeiouAEIOU')`），切片方向 `s[:mid]` = 前半、`s[mid:]` = 後半，方向容易寫反。

Trace (s = "book", mid = 2):
- front = s[:2] = "bo" → 'b','o' → 1 vowel
- back  = s[2:] = "ok" → 'o','k' → 1 vowel
- 1 == 1 → True

Mistake I made: `front, back = s[middle:], s[middle:]`（兩個切片都是後半）；`len(generator)` 不可用，應為 `sum()`；比較用 `!=` 邏輯反向，應為 `==`；pattern 誤識為 Sliding Window（此題無移動窗口，只有固定對切）。
