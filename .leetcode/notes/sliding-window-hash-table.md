# Sliding Window + Hash Table

### From: 567. Permutation in String (2026-07-11)

Input: s1 = "ab", s2 = "eidbaooo"
Approach: 用 Counter 記錄 s1 的字元頻率，對 s2 維護一個固定大小（len(s1)）的滑動視窗 Counter；每步移出最左字元、加入新字元，與 s1_count 比對。
Key insight: 排列問題等價於「字元頻率相同」，Counter 讓比較從 O(k!) 降到 O(|Σ|)；滑動視窗讓每步更新從 O(k) 降到 O(1)。

Trace（s1="ab", s2="eidbaooo"）：
- 初始視窗 "ei"：{'e':1,'i':1} ≠ {'a':1,'b':1}
- i=2 移出'e'加入'd' → {'i':1,'d':1} ≠
- i=3 移出'i'加入'b' → {'d':1,'b':1} ≠
- i=4 移出'd'加入'a' → {'b':1,'a':1} == {'a':1,'b':1} ✅ return True

Mistake I made: 空間複雜度誤答 O(n)——Counter 的 key 數上限是字母表大小 |Σ|=26，與輸入長度無關，應為 O(1)（或嚴謹寫 O(|Σ|)）。

---

### From: 2062. Count Vowel Substrings of a String (2026-07-11)

Input: word = "aeiouu"
Approach: 兩個左指針（left=連續母音段起點、start=包含所有 5 母音的最小起點）+ right 向右掃。遇子音三個指針同時重置。每輪 `result += start - left`，一次累加以 right 結尾的所有合法子字串數。
Key insight: 合法左端點的數量 = `start - left`，不是 `right - left - 5`。`start` 是 while 收縮後「剛好缺少某個母音」的第一個位置，所以 `[left, start-1]` 內的所有起點都合法。

Trace（word="aeiouu"）：
- right=0~3：have<5，result+=0
- right=4（u）：have=5，while 縮 start：word[0]='a' 計數→0 刪除，start=1。result += 1-0 = 1
- right=5（u）：have=4（a 已移除），while 不進入。result += 1-0 = 1 → total=2

Mistake I made: `substring[word[start]] -= 0` typo（應為 `-= 1`），導致 while 無限迴圈 IndexError；空間複雜度誤答 O(n)，字典最多 5 key 為 O(1)。
