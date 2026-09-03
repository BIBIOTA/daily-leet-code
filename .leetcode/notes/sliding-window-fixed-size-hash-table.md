# Sliding Window (Fixed Size) + Hash Table

### From: 567. Permutation in String (2026-09-04)

Input: s1 = "ab", s2 = "eidbaooo"
Approach: 先用 `Counter` 統計 `s1` 與 `s2` 前 `len(s1)` 個字元；之後從 index `len(s1)` 開始，每步移除離開視窗的字元、加入新字元，再比較兩個計數表。
Key insight: 候選子字串的長度一定是 `len(s1)`；當右端來到 index `i`，離開視窗的是 `s2[i - len(s1)]`。

Trace:
- 初始視窗 `"ei"`：`Counter({'e': 1, 'i': 1})`，不等於 `Counter("ab")`。
- i = 2：移除 `s2[0] = 'e'`、加入 `s2[2] = 'd'`，視窗成為 `"id"`。
- i = 3：移除 `s2[1] = 'i'`、加入 `s2[3] = 'b'`，視窗成為 `"db"`。
- i = 4：移除 `s2[2] = 'd'`、加入 `s2[4] = 'a'`，視窗成為 `"ba"`，計數相同而回傳 `True`。

Mistake I made: 把初始視窗寫成 `s2[len(s1):]`，它會從該 index 取到結尾，不是前 `len(s1)` 個字元；應為 `s2[:len(s1)]`。另外離開字元曾寫成 `s2[i - len(s1) - 1]`，第一次滑動會錯取 `s2[-1]`；正確索引是 `s2[i - len(s1)]`。
