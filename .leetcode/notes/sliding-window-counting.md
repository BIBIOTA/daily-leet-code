# Sliding Window (Counting)

> 計數型滑動視窗：數的不是「最長/最短」，而是「合格子字串/子陣列的**個數**」。
> 招牌動作 —— `res += (right_pointer - left_pointer)`：一次把「以當前右端結尾的所有合法起點」整批加進去，不是逐一 `+= 1`。

---

### From: 2062. Count Vowel Substrings of a String (2026-07-09)

Input: `word = "cuaieuouac"` → `7`；`word = "aeiouu"` → `2`
Approach: 對每個右端點 `right`，用收縮指標 `start` 往右縮到「`[start, right]` 剛好不再集滿五母音」，則合法起點是 `[left, start-1]`，個數 = `start - left`；碰到子音把整段母音視窗歸零（`left = start = right + 1`）。
Key insight: 「以右端點結尾的合格子字串**個數**」= 「合法起點能滑動的範圍長度」。每個右端點該加的量會變動，用 `start - left` 一次算出整批。

Trace（`"aeioua"`，全母音故 left 恆 0）:
- right=4 (u) 首次集滿 → while 縮掉 word[0]=a → start=1 → `res += 1-0 = 1`（起點只有 0 → "aeiou"）
- right=5 (a) 又集滿 → while 縮掉 word[1]=e → start=2 → `res += 2-0 = 2`（起點 0,1 → "aeioua","eioua"）
- 合計 3 ✅

Complexity: 時間 O(n)（`right` 與 `start` 各單向前進 ≤ n 次，巢狀 while 不是 O(n²)）；空間 O(1)（cnt 最多 5 個 key）。

Mistake I made:
- 反覆在「求長度 / max」和「計數」之間打轉 —— 用 `len(substrings)`、`max_count` 而非累加合格配對數。
- 中途 `return`（第一次集滿就收工），應掃完整個字串把每段貢獻加總。
- 判斷五母音齊全用「長度 == 5」而非「set == vowels」——漏掉長度 > 5 仍合格的段（如 "aeiouu"）。
- 語法坑：`list.append()` 忘了傳參數、`return x += 1`（+= 是語句不能接在 return 後）。
- 核心卡點：不知道「集滿時該加幾」，缺少顯式的 `left` 左界指標 —— 這正是計數型視窗的鑰匙。

變體練習（吃透 pattern）:
- 若改成「允許中間夾子音、只要含全部 5 種母音」→ **移除**「子音重置」與 `seg_start`（`res += lo - left` 簡化為 `res += lo`），但 **while 收縮迴圈必須保留**（它是計數引擎，不是原題的額外約束）。縮指標跨過子音時 distinct 不變，天然可跨。

相關題目: 992 (Subarrays with K Different Integers)、1358 (Number of Substrings Containing All Three Characters)、713 (Subarray Product Less Than K) —— 都是「數連續子區間個數」的計數型視窗。

---

### From: 438. Find All Anagrams in a String (2026-07-19)

Input: `s = "cbaebabacd"`, `p = "abc"` → `[0, 6]`
Approach: 建固定大小視窗（長度 = len(p)），用 Counter 比對視窗與 p 的字元頻率是否完全相同；滑動時移除最左字元、加入最右字元，維護 running Counter。
Key insight: 每步只需 O(1) 更新兩個字元計數（移除 s[i-len(p)]、加入 s[i]），避免每輪重建 Counter 的 O(m) 代價，將總時間從 O(n×m) 降至 O(n)。

Trace（s="cbaebabacd", p="abc"，視窗大小=3）:
- 初始視窗 "cba"：Counter={'c':1,'b':1,'a':1} == p_count → append 0
- i=3：移除 s[0]='c'，加入 s[3]='e' → {'b':1,'a':1,'e':1} ≠ p_count
- i=4：移除 s[1]='b'，加入 s[4]='b' → {'a':1,'e':1,'b':1} ≠ p_count
- i=6：移除 s[3]='e'，加入 s[6]='b' → {'a':1,'b':1,'c':1} == p_count → append 6

Mistake I made: 用 `Counter(s[i:i+p_len])` 每輪重建，誤以為時間是 O(n)，實際是 O(n×m)；不知道「進一個、出一個」的 O(1) 維護方式。

---

### Review: 2062. Count Vowel Substrings of a String (2026-07-10)

Mistake I made（複習仍重蹈的坑）:
- 遇子音只 `continue` 跳過，但沒有清空 `vowel_dict`，導致跨子音的母音被合算進同一視窗。
- `while` 迴圈內縮的是右端 `ch`，應縮左端 `word[start]`。
- 只用一個左指標，缺少 `left`（段起點）與 `start`（可收縮指標）兩者分離的概念。
- 無法解釋「start 為何不後退」：答案就是程式碼中 start 只有 `start += 1`，沒有任何 `start -= 1`，天然單調遞增，攤銷 O(n)。
