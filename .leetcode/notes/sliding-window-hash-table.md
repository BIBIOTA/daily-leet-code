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
